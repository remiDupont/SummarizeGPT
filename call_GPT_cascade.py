""" File to call chatGPT4 to make summary of a texte """

from openai import OpenAI
import datetime
from call_GPT import read_file, call_chat_gpt, analyze_num_tokens, ma_prompt, save_file
from constants import ma_prompt_cascade, ma_prompt_cascade_serie
import glob
import os

client = OpenAI()


def process_script_blocks(file_list, model="gpt-3.5-turbo-1106"):
    # remove all files in ./temp_markdown
    temp_folder = "./temp_markdown"
    [
        os.remove(os.path.join(temp_folder, f))
        for f in os.listdir(temp_folder)
        if os.path.isfile(os.path.join(temp_folder, f))
    ]

    markdown_list = []
    for i, file in enumerate(file_list):
        texte = read_file(file)

        gpt_input = (
            ma_prompt_cascade
            + " /n  < Début du texte >  : "
            + texte
            + " /n < Fin du texte >"
        )

        analyze_num_tokens(gpt_input, is_GPT35Turbo=model == "gpt-3.5-turbo-1106")
        markdown_element = call_chat_gpt(model=model, prompt=gpt_input)
        markdown_list.append(markdown_element)
        save_file(
            f"./temp_markdown/{model}-{ file.split('/')[-1].replace('.txt','.md') }",
            markdown_element,
        )

    markdown_concat = " /n ".join(markdown_list)
    final_file_path = (
        f"./temp_markdown/concat-{ file.split('/')[-1].replace('.txt','.md') }"
    )

    save_file(
        final_file_path,
        markdown_concat,
    )
    return final_file_path


def process_stacked_markdown(final_file_path, model="gpt-4-1106-preview"):
    with open(final_file_path) as file:
        concatenated_markdown = file.read()

    gpt_input = (
        "Reorganise le texte en ne modifiant que les titres : tu dois impérativement garder le contenu exact de tous les paragraphes mais tu peux renommer les titres et bouger les paragraphes afin d'avoir un texte plus cohérents. Tous les paragraphes doivent être recopiées, sans AUCUNE modifications. ta réponse doit recopier l'ensemble des paragraphes, dans leur integralité.  < Début du markdown >  : "
        + concatenated_markdown
        + " /n < Fin du markdown >"
    )
    analyze_num_tokens(gpt_input, is_GPT35Turbo=False)
    final_markdown = call_chat_gpt(model=model, prompt=gpt_input)
    save_file(
        f"./resultat_final/{final_file_path.split('/')[-1].replace('concat-','')}",
        final_markdown,
    )


def main():
    # lit les données
    file_list = glob.glob("./transcriptions/EPR-28-S5-1-TriadeSante_*")
    file_list.sort()

    # process les données
    final_file_path = process_script_blocks(file_list, model="gpt-3.5-turbo-1106")
    process_stacked_markdown(final_file_path, model="gpt-4-1106-preview")


if __name__ == "__main__":
    main()
    print("Done")
