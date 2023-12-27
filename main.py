import wisper
import call_GPT_cascade
import argparse
import os
import constants


def get_args():
    parser = argparse.ArgumentParser(description="Process a filename.")
    parser.add_argument(
        "input_dir_or_file", type=str, help="The name of the file to process"
    )
    return parser.parse_args()


def apply_pipeline(file_path):
    # transcribe the file
    extension = file_path.split(".")[-1].lower()
    if extension in constants.supported_extensions:
        wisper.mainTranscribe(file_path)
        call_GPT_cascade.main(file_path.split("/")[-1].split(".")[0])


if __name__ == "__main__":
    args = get_args()

    if os.path.isfile(args.input_dir_or_file):
        apply_pipeline(args.input_dir_or_file)

    if os.path.isdir(args.input_dir_or_file):
        for file in os.listdir(args.input_dir_or_file):
            apply_pipeline(os.path.join(args.input_dir_or_file, file))
