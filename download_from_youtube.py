from pytube import YouTube


def get_title(yt, video):
    return (
        yt.title.replace(" ", "_").replace(":", "").replace("&", "")[:20]
        + "."
        + video.mime_type.split("/")[-1]
    )


def download_url(url):
    # Création d'un objet YouTube
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()

    # Téléchargement de la vidéo
    video.download("./download", get_title(yt, video))

    print("Téléchargement terminé!")


url_list = [
    # "https://www.youtube.com/watch?v=8OHYynw7Yh4"
    # "https://www.youtube.com/watch?v=xLORsLlcT48"
    # "https://www.youtube.com/watch?v=50BZQRT1dAg",
    # "https://www.youtube.com/watch?v=3gtvNYa3Nd8",
    # "https://www.youtube.com/watch?v=wAZn9dF3XTo",
    # "https://www.youtube.com/watch?v=pkJi9Raxikg",
    # "https://www.youtube.com/watch?v=CJIXbibQ0jI",
    # "https://www.youtube.com/watch?v=FeRgqJVALMQ",
    # "https://www.youtube.com/watch?v=eMqWH3LYiII",
    # "https://www.youtube.com/watch?v=qPKd99Pa2iU",
    # "https://www.youtube.com/watch?v=aQDOU3hPci0",
    # "https://www.youtube.com/watch?v=slUCmZJDXrk",
    # "https://www.youtube.com/watch?v=6ZrlsVx85ek",
    # "https://www.youtube.com/watch?v=K-TW2Chpz4k",
    # "https://www.youtube.com/watch?v=CGjdgy0cwGk",
    # "https://www.youtube.com/watch?v=xJ0IBzCjEPk",
    # "https://www.youtube.com/watch?v=xJ0IBzCjEPk",
    "https://www.youtube.com/watch?v=szqPAPKE5tQ&ab_channel=AndrewHuberman"
]


for url in url_list:
    download_url(url)
