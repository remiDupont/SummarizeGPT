from transformers import GPT2Tokenizer
import PyPDF2


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


def extraire_texte_pdf(chemin_fichier):
    with open(chemin_fichier, 'rb') as fichier:
        lecteur_pdf = PyPDF2.PdfReader(fichier)
        nombre_pages = len(lecteur_pdf.pages)
        texte = ''

        for num_page in range(nombre_pages):
            page = lecteur_pdf.pages[num_page]
            texte += page.extract_text() + "\n"

    return texte



def test_sur_un_texte():
    # Votre texte
    file_path = "/Users/remi/Desktop/DavidLaroche/ami.pdf"

    with open(file_path, 'r') as file:
        text = file.read()

    # Tokeniser le texte
    tokens = tokenizer.encode(text)

    # Compter le nombre de tokens
    number_of_tokens = len(tokens)

    # Afficher le nombre de tokens

    print(f"Nombre de tokens: {number_of_tokens}")


def get_number_of_tokens(text):
    # Tokeniser le texte
    tokens = tokenizer.encode(text)

    # Compter le nombre de tokens
    number_of_tokens = len(tokens)

    # Retourner le nombre de tokens
    return number_of_tokens

