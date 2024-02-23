from pytube import YouTube


def get_title(yt, video):
    return (
        yt.title.replace(" ", "_").replace(":", "").replace("&", "")[:70]
        + "."
        + video.mime_type.split("/")[-1]
    )


def download_url(url:str):

    # Création d'un objet YouTube
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()

    # Téléchargement de la vidéo
    video.download("./data/input", get_title(yt, video))

    print("Téléchargement terminé!")


url_list = [
    "https://www.youtube.com/watch?v=8OHYynw7Yh4",
    # "https://www.youtube.com/watch?v=yb5zpo5WDG4",
#    "https://www.youtube.com/watch?v=eMqWH3LYiII"
]


for url in url_list:
    download_url(url)
