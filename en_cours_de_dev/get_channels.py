from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os 

def get_channel_id(youtube, username):
    try:
        response = youtube.channels().list(forUsername=username, part='id').execute()
        return response['items'][0]['id']
    except (IndexError, KeyError):
        return None

def get_video_urls(youtube, channel_id):
    video_urls = []
    next_page_token = None

    while True:
        try:
            response = youtube.search().list(
                channelId=channel_id,
                part='id',
                maxResults=50,
                pageToken=next_page_token,
                type='video'
            ).execute()

            video_ids = [item['id']['videoId'] for item in response.get('items', [])]
            video_urls.extend(['https://www.youtube.com/watch?v=' + vid for vid in video_ids])

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        except HttpError as e:
            print('An HTTP error occurred:', e.resp.status, e.content)
            break

    return video_urls

# Clé API et construction du service
api_key = os.environ.get('API_KEY_YOUTUBE')
youtube = build('youtube', 'v3', developerKey=api_key)

# Nom d'utilisateur de la chaîne YouTube
username = 'balexdevperso8329'


channelID = '11111111'

request = youtube.search().list(
    part='id',
    channelId=channelID,
    type='video',
    order='date',
    maxResults=50
)

response = request.execute()


# # Obtenir l'ID de la chaîne à partir du nom d'utilisateur
# channel_id = get_channel_id(youtube, username)
# if channel_id:
#     print("ID de la chaîne:", channel_id)
#     # Récupérer et afficher les URL des vidéos
#     video_urls = get_video_urls(youtube, channel_id)
#     for url in video_urls:
#         print(url)
# else:
#     print("La chaîne n'a pas été trouvée.")
