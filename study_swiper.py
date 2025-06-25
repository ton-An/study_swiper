import click
import time
from yaspin import yaspin

@click.group()
def cli():
    """Swipes decks from Study Smarter (Vaia)"""
    pass

@cli.command()
@click.argument('decks', nargs=-1)
@click.option('--username', prompt=True, help='Your StudySmarter username')
@click.option('--password', prompt=True, hide_input=True, help='Your StudySmarter password')
def run(decks, username, password):
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


    if len(decks) == 0:
        # Prompt for deck IDs
        deck_input = click.prompt('Enter deck IDs (space-separated)', default='', show_default=False)
        decks = deck_input.split()

        if len(decks) == 0:
            click.echo(
                click.style('Please specify at least one deck id. For help run study_swiper run --help', fg='red'))
            return

    auth_token = get_auth_token(username, password)


def get_auth_token(username, password):
    with yaspin(text="Authenticating", color="cyan") as spinner:
        try:
            # Your authentication logic here
            time.sleep(2)  # Simulate auth delay

            spinner.ok("✓")  # Show success
            click.echo(click.style('Authentication successful', fg='green'))

            return "your_auth_token"

        except Exception as e:
            spinner.fail("✗")  # Show failure
            click.echo(click.style(f'Authentication failed: {str(e)}', fg='red'))
            raise e