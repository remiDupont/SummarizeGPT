""" File to call chatGPT4 to make summary of a texte """

from openai import OpenAI
from call_GPT import read_file, call_chat_gpt, analyze_num_tokens, ma_prompt, save_file
from constants import ma_prompt_cascade, ma_prompt_cascade_serie2
import constants
import glob
import os
import argparse


client = OpenAI(api_key=os.getenv('OPENAI_KEY'))


def process_script_blocks(file_list, final_output_dir=None):
    # remove all files in ./temp_markdown
    temp_folder = "./data/temp_markdown"
    [
        os.remove(os.path.join(temp_folder, f))
        for f in os.listdir(temp_folder)
        if os.path.isfile(os.path.join(temp_folder, f))
    ]

    markdown_list = []
    for file in file_list:
        texte = read_file(file)
        gpt_input = (
            ma_prompt_cascade
            + " /n  < Début du texte >  : "
            + texte
            + " /n < Fin du texte >"
        )
        analyze_num_tokens(gpt_input, cost_per_token=constants.base_model["cost_per_token"])
        markdown_element = call_chat_gpt(model=constants.base_model["model"], prompt=gpt_input)
        markdown_list.append(markdown_element)
        save_file(
            f"./data/temp_markdown/{constants.base_model["model"]}-{ file.split('/')[-1].replace('.txt','.md') }",
            markdown_element,
        )

    markdown_concat = " /n ".join(markdown_list)
    if final_output_dir is not None:
        final_output_dir = f"{final_output_dir}/"
    else:
        final_output_dir = "./data/temp_markdown"

    final_file_path = (
        f"{final_output_dir}/concat-{ file.split('/')[-1].replace('.txt','.md') }"
    )

    save_file(
        final_file_path,
        markdown_concat,
    )
    return final_file_path


def process_stacked_markdown(
    final_file_path, model, final_output_dir="./Résumes"
):
    with open(final_file_path) as file:
        concatenated_markdown = file.read()

    gpt_input = (
        ma_prompt_cascade_serie2
        + concatenated_markdown
        + " /n < Fin du markdown >"
    )
    analyze_num_tokens(gpt_input, cost_per_token=constants.modele_agregation["cost_per_token"])
    final_markdown = call_chat_gpt(model=model, prompt=gpt_input)
    save_file(
        f"{final_output_dir}/{final_file_path.split('/')[-1].replace('concat-','')}",
        final_markdown,
    )


def main(filename, final_output_dir):
    # lit les scripts
    file_list = glob.glob(f"./data/transcriptions/{filename}*.txt")
    if len(file_list) > 1:  # match only subfiles
        file_list = glob.glob(f"./data/transcriptions/{filename}_*.txt")
    file_list.sort()

    # process les données
    final_file_path = process_script_blocks(file_list, final_output_dir)
    # process_stacked_markdown(
    #     final_file_path=final_file_path,
    #     model=constants.modele_agregation["model"],
    #     final_output_dir=final_output_dir,
    # )


if __name__ == "__main__":
    # EPR-28-S5-1-TriadeSante
    parser = argparse.ArgumentParser(description="Process a filename.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    args = parser.parse_args()
    print(f"Filename provided: {args.filename}")
    main(args.filename)
