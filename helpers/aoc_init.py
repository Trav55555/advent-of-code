import os
import pathlib
from aocd import get_data
import argparse

BASE_URL = "https://adventofcode.com"


if __name__ == "__main__":
    current_dir = pathlib.Path().resolve()
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--year",
        help="The year of advent of code to generate directories and input files for.",
        default="2023",
    )
    parser.add_argument(
        "filepath",
        help="The path of the directory to use as the root dir.",
        default=current_dir,
    )

    args = parser.parse_args()

    root_path = args.filepath
    year = args.year

    if not os.path.exists(f"{root_path}/{year}"):
        os.makedirs(f"{root_path}/{year}")

    for i in range(25):
        day = i + 1
        prefix = ""
        if day < 10:
            prefix = "0"

        new_path = f"{root_path}/{year}/{prefix}{day}"

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        input_path = f"{new_path}/input.txt"

        with open(input_path, "w") as file:
            data = get_data(day=day, year=year)
            file.write(data)
