import whisper
import os
import time
from token_counter import get_number_of_tokens
import argparse

model_name = ["tiny", "small", "medium"][2]


def couper_txt_en_segments(texte, n):
    text_list = texte.split()
    num_words = len(text_list)
    num_worlds_per_segment = num_words / n

    idx_list = [int(num_worlds_per_segment * i) for i in range(n)] + [num_words]
    result_list = []

    for i in range(n):
        result_list.append(" ".join(text_list[idx_list[i] : idx_list[i + 1]]))

    return result_list


def isvideo(file_path):
    return (
        file_path.endswith(".mp4")
        or file_path.endswith(".mkv")
        or file_path.endswith(".avi")
    )


def extract_audio(file_path):
    base_path, _ = os.path.splitext(file_path)
    output_file = base_path + ".mp3"

    # Écrire la transcription dans le fichier
    os.system(f"ffmpeg -i {file_path} -y -ab 160k -ac 2 -ar 44100 -vn {output_file}")
    # os.system("ffmpeg -i {file_path} -y -c:a aac -b:a 128k -ac 2 -ar 44100 -vn {output_file}")

    os.remove(file_path)
    return output_file


def transcribe_media(file_path):
    if isvideo(file_path):
        file_path = extract_audio(file_path)

    # Charger le modèle Whisper
    # tiny = 17 sec, bad quality #small = 64 sec, qualité tres bonne, medium : qualité nickel, 212.7 ==> temps reel
    print(f"Chargement du modèle {model_name}")

    model = whisper.load_model(model_name)

    # Transcrire l'audio
    return model.transcribe(file_path, verbose=True)["text"]


def get_destination_name(file_path):
    # Obtenir le chemin de base et le nom du fichier sans extension
    base_path, _ = os.path.splitext(file_path)
    # Créer le nom du fichier de sortie avec l'extension .txt
    return "./data/transcriptions/" + base_path.split("/")[-1] + ".txt"


def save_transcription(file_path, transcription):
    # Écrire la transcription dans le fichier
    gpt4_max_tokens = 7900

    num_tokens = get_number_of_tokens(transcription)
    with open(get_destination_name(file_path), "w") as file:
        file.write(transcription)

    if num_tokens > gpt4_max_tokens:
        num_chunks = num_tokens // gpt4_max_tokens + 1
        for i, segment in enumerate(couper_txt_en_segments(transcription, num_chunks)):
            with open(get_destination_name(file_path)[:-4] + f"_{i}.txt", "w") as file:
                file.write(segment)


def mainTranscribe(file_path):
    # Appeler la fonction et obtenir la transcription
    if os.path.exists(get_destination_name(file_path)):
        print(f"Transcription déjà effectuée pour ce fichier : {file_path}")
        return
    else:
        start_time = time.time()
        transcription = transcribe_media(file_path)
        end_time = time.time()
        print(f"Temps d'exécution: {end_time - start_time} secondes")

        # Afficher la transcription
        # Sauvegarder la transcription dans un fichier texte
        save_transcription(file_path, transcription)


# Spécifier le chemin de votre fichier audio
# def main(media_path):
#     # file_path = "/Users/remi/Desktop/DavidLaroche/Entraine pour reussir/EPR-28-S5-1-TriadeSante.mp3"
#     mainTranscribe(media_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a filename.")
    parser.add_argument("mediapath", type=str, help="The name of the file to process")
    args = parser.parse_args()
    mainTranscribe(args.mediapath)


# liste l'ensemble des fichiers dans le dossier

# directory_name = "/Users/remi/Desktop/DavidLaroche/Input0-10/"
# for file in os.listdir(directory_name):
#     if file.endswith(".mp3"):
#         mainTranscribe(directory_name + file)
