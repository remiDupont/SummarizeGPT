# import wisper
import call_GPT_cascade
import argparse
import os
import constants
import wisper
from pathlib import Path


def cretate_dir_if_not_exists(dir_path):
    """Create a directory if it does not exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_args():
    """Get the arguments from the command line."""
    parser = argparse.ArgumentParser(description="Process a filename.")
    parser.add_argument(
        "--input_dir_or_file", type=str, help="The name of the file to process"
    )
    parser.add_argument(
        "--final_output_dir",
        type=str,
        help="The name of the file to process",
        default="./Resumes",
    )
    parser.add_argument(
        "--keep_folders", help="keep folders structure", action='store_true'
    )
    return parser.parse_args()


def apply_pipeline_to_file(file_path, final_output_dir):
    """Apply the pipeline to a file."""

    # if the file_path contains spaces, move it to a new file without spaces
    if " " in file_path:
        new_file_path = file_path.replace(" ", "_")
        os.rename(file_path, new_file_path)
        file_path = new_file_path
    
    extension = file_path.split(".")[-1].lower()
    if extension in constants.supported_extensions:
        wisper.mainTranscribe(file_path)
        call_GPT_cascade.main(
            filename=file_path.split("/")[-1].split(".")[0],
            final_output_dir=final_output_dir,
        )


if __name__ == "__main__":
    args = get_args()

    cretate_dir_if_not_exists(args.final_output_dir)

    if os.path.isfile(args.input_dir_or_file):
        apply_pipeline_to_file(args.input_dir_or_file, args.final_output_dir)

    if os.path.isdir(args.input_dir_or_file):
        for fichier in Path(args.input_dir_or_file).rglob('*'):
            if fichier.is_file():
                print(f"Processing file: {fichier} in {args.input_dir_or_file}")

                # Calculer le chemin relatif du sous-dossier contenant le fichier
                sous_dossier = fichier.parent.relative_to(args.input_dir_or_file)
                print(f"Fichier: {fichier}, Sous-dossier: {sous_dossier}")
                
                final_output_dir = os.path.join(args.final_output_dir, sous_dossier)
                cretate_dir_if_not_exists(final_output_dir)

                apply_pipeline_to_file(
                    fichier._str, final_output_dir
                )


                

    # for file in os.listdir(args.input_dir_or_file):
    #     apply_pipeline_to_file(
    #         os.path.join(args.input_dir_or_file, file), args.final_output_dir
    #     )
