import click
from yaspin import yaspin
import uuid
import requests
import re
from bs4 import BeautifulSoup
import urllib.request

@click.group()
def cli():
    """Swipes decks from Study Smarter (Vaia)"""
    pass

@cli.command()
@click.argument('deck_ids', nargs=-1)
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

    decks = get_decks(auth_token, deck_ids)

    parsed_decks = parse_decks(decks)

    print(parsed_decks)

    #save_images(parsed_decks)

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
    with yaspin(text='Fetching decks', color='cyan') as spinner:
        try:
            decks = []

            request_headers = {
                'Accept': 'application/json',
                'Authorization': f'Token {auth_token}',
            }

            for index, deck_id in enumerate(deck_ids):
                spinner.text = f'Fetching deck {deck_id} - {index + 1}/{len(deck_ids)}'
                cards_url = f'https://prod.studysmarter.de/studysets/{deck_id}/flashcards/?search=&s_bad=true&s_medium=true&s_good=true&s_trash=false&s_unseen=true&tag_ids=&quantity=20&all=true&order=anti-chronological'
                tags_url = f'https://prod.studysmarter.de/studysets/{deck_id}/tags/?content_filter=flashcards'

                cards = get_cards(cards_url, request_headers, deck_id, [])
                tags = get_tags(tags_url, request_headers, deck_id)

                deck = {
                    'id': deck_id,
                    'cards': cards,
                    'tags': tags,
                }
                decks.append(deck)

            spinner.color = 'green'
            spinner.text = 'Decks successfully fetched'
            spinner.ok('✓')

            return decks

        except Exception as e:
            spinner.color = 'red'
            spinner.text = 'Fetching decks failed'
            spinner.fail('✗')
            click.echo(click.style(str(e), fg='red'))
            raise e

def get_cards(url, request_headers, deck_id, existing_cards):
    request = requests.get(url, headers=request_headers)

    status_code = request.status_code

    cards_json = request.json()

    if status_code != 200:
        raise Exception(f'Fetching Cards failed: Status code {status_code} - Deck ID {deck_id} -- Server Response: {cards_json}')


    cards = existing_cards + cards_json["results"]

    if cards_json["next"] is not None:
        return get_cards(cards_json["next"], request_headers, deck_id, cards)
    else:
        return cards

def get_tags(url, request_headers, deck_id):
    request = requests.get(url, headers=request_headers)

    status_code = request.status_code

    tags_json = request.json()

    if status_code != 200:
        raise Exception(f'Fetching Tags failed: Status code {status_code} - Deck ID {deck_id} -- Server Response: {tags_json}')

    return tags_json['all_parent_tags']

def parse_decks(decks):
    with yaspin(text='Fetching decks', color='cyan') as spinner:
        try:
            parsed_decks = []

            for deck in decks:
                deck_id = deck['id']
                cards = deck['cards']
                tags = deck['tags']

                spinner.text = f'Parsing deck {deck_id}'

                parsed_cards = []
                for card in cards:
                    front = parse_card_side(card["question_html"][0]["text"])
                    back = parse_card_side(card["answer_html"][0]["text"])
                    applied_tags = map_tags(card["community_applied_tag_ids"], tags)

                    parsed_card = {
                        'front': front,
                        'back': back,
                        'tags': applied_tags,
                    }
                    parsed_cards.append(parsed_card)

                parsed_deck = {
                    'deck_id': deck_id,
                    'cards': parsed_cards,
                }
                parsed_decks.append(parsed_deck)


            spinner.color = 'green'
            spinner.text = 'Decks successfully parsed'
            spinner.ok('✓')

            return parsed_decks

        except Exception as e:
            spinner.color = 'red'
            spinner.text = 'Parsing decks failed'
            spinner.fail('✗')
            click.echo(click.style(str(e), fg='red'))
            raise e

def parse_card_side(card_side):
    sanitized_card_side = card_side.replace("&amp;", "&").replace("‐", "-")

    soup = BeautifulSoup(sanitized_card_side, 'html.parser')

    images = soup.findAll('img')

    image_urls = []

    for image in images:
        try:
            file_name = re.search(r'[^/]+(?=\?X-Amz)', image['src']).group(0)
        except:
            continue

        image_urls.append(image['src'])

        image['src'] = file_name

    return {
        'images': image_urls,
        'parsed_card_side': str(soup),
    }

def map_tags(tag_ids, tags):
    applied_tags = ""
    for tag_id in tag_ids:
        for tag in tags:
            if tag["id"] == tag_id:
                tag_name = tag["name"].replace("‐", "-").replace(":", "").replace(" ", "::").replace("-", "_").replace(
                    "_/", "-/")
                applied_tags += tag_name + " "
    return applied_tags
