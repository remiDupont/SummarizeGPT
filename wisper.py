import whisper
import os

def transcribe_audio(file_path):
    # Charger le modèle Whisper
    model = whisper.load_model("tiny")

    # Transcrire l'audio
    result = model.transcribe(file_path)

    # Retourner la transcription
    return result["text"]

def save_transcription(file_path, transcription):
    # Obtenir le chemin de base et le nom du fichier sans extension
    base_path, _ = os.path.splitext(file_path)

    # Créer le nom du fichier de sortie avec l'extension .txt
    output_file = base_path + ".txt"

    # Écrire la transcription dans le fichier
    with open(output_file, 'w') as file:
        file.write(transcription)

# Spécifier le chemin de votre fichier audio
file_path = "/Users/remi/Desktop/David Laroche/Entraine pour reussir/EPR-28-S5-1-TriadeSante.mp3"
# file_path = "/Users/remi/Desktop/debug.mp3"


# Appeler la fonction et obtenir la transcription
transcription = transcribe_audio(file_path)

# Sauvegarder la transcription dans un fichier texte
save_transcription(file_path, transcription)
