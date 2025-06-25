import click
from yaspin import yaspin
import uuid
import requests

@click.group()
def cli():
    """Swipes decks from Study Smarter (Vaia)"""
    pass

@cli.command()
@click.argument('decks', nargs=-1)
@click.option('--username', prompt=True, help='Your StudySmarter username')
@click.option('--password', prompt=True, hide_input=True, help='Your StudySmarter password')
def run(deck_ids, username, password):
    """Download flashcard decks from StudySmarter by their IDs.

    Deck ids are the IDs of the decks you want to download. You can specify
    multiple deck IDs separated by spaces.

    \b
    How to find deck IDs:
    Extract the numeric ID from the StudySmarter deck URL.

    \b
    Example URL:
    https://app.vaia.com/studyset/934059?trackingSource=studysets_library&tab=library
    The deck ID is: 934059

    \b
    Examples:
        # Download a single deck
        study_swiper run 934059 --username ted --password mosbius123

        # Download multiple decks
        study_swiper run 934059 123456 789012 --username ted --password mosbius123

        # Interactive mode (prompts for all required parameters)
        study_swiper run
    """


    if len(deck_ids) == 0:
        deck_input = click.prompt('Enter deck IDs (space-separated)', default='', show_default=False)
        deck_ids = deck_input.split()

        if len(deck_ids) == 0:
            click.echo(
                click.style('Please specify at least one deck id. For help run study_swiper run --help', fg='red'))
            return

    auth_token = get_auth_token(username, password)

    # decks = get_decks(auth_token, deck_ids)
    #
    # save_decks_to_csv(decks)



def get_auth_token(username, password):
    with yaspin(text='Authenticating', color='cyan') as spinner:
        try:
            auth_url = 'https://prod.studysmarter.de/api-token-auth/'

            amplitude_device_id = uuid.uuid4()

            auth_request_body = {
                'amplitude_device_id': str(amplitude_device_id),
                'password': password,
                'platform': 'webapp',
                'username': username,
            }

            request =  requests.post(auth_url, json= auth_request_body)

            status_code = request.status_code

            response_body = request.json()

            errors = response_body.get('errors', [])

            if len(errors) > 0:
                raise Exception(f'Authentication failed with status code: {status_code} and errors: {errors}')

            access_token = response_body['token']

            spinner.color = 'green'
            spinner.text = 'Authentication successful'
            spinner.ok('✓')

            return access_token


        except Exception as e:
            spinner.color = 'red'
            spinner.text = 'Authentication failed'
            spinner.fail('✗')
            click.echo(click.style(str(e), fg='red'))
            raise e

def get_decks(auth_token, deck_ids):
    click.echo('Fetching decks...')