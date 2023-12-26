from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
url = 'http://youtube.com/watch?v=2lAe1cqCOXo'

def download_url(url):

    # Création d'un objet YouTube
    yt = YouTube(url)

    # Sélection de la première résolution de flux disponible
    video = yt.streams.filter(progressive=True, file_extension='mp4').first()

    # Afficher des détails sur la vidéo
    print("Titre :", yt.title)
    print("Longueur de la vidéo :", yt.length, "secondes")
    print("Résolution de la vidéo sélectionnée :", video.resolution)

    # Téléchargement de la vidéo
    video.download()

    print("Téléchargement terminé!")


# from pytube import Channel
# c = Channel('https://www.youtube.com/@whosgonnacarrytheboats7')
# print(c.video_urls)
# for video in c.video_urls:
#     print(video)









api_key=os.environ.get('API_KEY_YOUTUBE')
youtube=build(
    'youtube',
    'v3',
    developerKey=api_key
)

#Make a request to youtube api
request = youtube.channels().list(
    part='contentDetails',
    forUsername='DisneyMusicVEVO' 
  #you can change the channel name here
)


#get a response for api
response=request.execute()
print(response)

# Retrieve the uploads playlist ID for the given channel
playlist_id=response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Retrieve all videos from uploads playlist
videos = []
next_page_token = None

while True:
    playlist_items_response=youtube.playlistItems().list(
                #part='contentDetails',
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
    ).execute()

    videos += playlist_items_response['items']

    next_page_token = playlist_items_response.get('nextPageToken')

    if not next_page_token:
        break

# Extract video URLs
video_urls = []

for video in videos:
    #video_id = video['contentDetails']['videoId']
    video_id = video['snippet']['resourceId']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_title=video['snippet']['title']
    #video_urls.append(video_url)
    video_urls.append({'URL':video_url,'Title':video_title})

#return video_urls

#open file
outFile=open("YoutubeVideos.txt", "w",encoding="utf-8")
outFile.write("URL,Title\n")
# Print the extracted video URLs
for key in video_urls:
    line=key['URL']+","+key['Title']+"\n"
    outFile.write(line)