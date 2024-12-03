import os
import pathlib
from aocd import get_data
import argparse
import time
from datetime import datetime

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

    # if we are in or before december of that year, only generate the days that have passed
    # otherwise generate all days

    current_date = datetime.now()
    x = 25
    if current_date.year <= int(year):
        if current_date.month < 12:
            x = 0
        elif current_date.month == 12:
            x = current_date.day

    for i in range(x):
        day = i + 1
        prefix = ""
        if day < 10:
            prefix = "0"

        new_path = f"{root_path}/{year}/{prefix}{day}"

        if not os.path.exists(new_path):
            os.makedirs(new_path)

        input_path = f"{new_path}/input.txt"

        with open(input_path, "w") as file:
            try:
                data = get_data(day=day, year=year)
                file.write(data)
                time.sleep(0.5)
            except Exception as e:
                print(f"Failed to get data for day {day} year {year}")
                print(e)
                file.write("")
