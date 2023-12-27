# import wisper
import call_GPT_cascade
import argparse
import os
import constants


def cretate_dir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_args():
    parser = argparse.ArgumentParser(description="Process a filename.")
    parser.add_argument(
        "--input_dir_or_file", type=str, help="The name of the file to process"
    )
    parser.add_argument(
        "--final_output_dir",
        type=str,
        help="The name of the file to process",
        default="./Résumes",
    )
    return parser.parse_args()


def apply_pipeline(file_path, final_output_dir):
    extension = file_path.split(".")[-1].lower()
    if extension in constants.supported_extensions:
        # wisper.mainTranscribe(file_path)
        call_GPT_cascade.main(
            filename=file_path.split("/")[-1].split(".")[0],
            final_output_dir=final_output_dir,
        )


if __name__ == "__main__":
    args = get_args()

    cretate_dir_if_not_exists(args.final_output_dir)

    if os.path.isfile(args.input_dir_or_file):
        apply_pipeline(args.input_dir_or_file, args.final_output_dir)

    if os.path.isdir(args.input_dir_or_file):
        for file in os.listdir(args.input_dir_or_file):
            apply_pipeline(
                os.path.join(args.input_dir_or_file, file), args.final_output_dir
            )
