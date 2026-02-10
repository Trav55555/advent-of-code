"""CLI for Advent of Code project management.

Commands:
    new <year> <day>        Scaffold a new day (dirs, template files, download input)
    run <year> <day> <part> Run a solution with input.txt
    test <year> <day> <part> Run a solution with test.txt
    download <year>         Bulk-download all available inputs for a year
"""

import argparse
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from helpers.template import SOLUTION_TEMPLATE


def get_project_root() -> Path:
    """Return the project root (parent of helpers/)."""
    return Path(__file__).resolve().parent.parent


def day_dir(year: int, day: int) -> Path:
    """Return the path to a day's directory."""
    return get_project_root() / str(year) / f"{day:02d}"


def cmd_new(args: argparse.Namespace) -> None:
    """Scaffold a new day: create directory, template files, download input."""
    year = args.year
    day = args.day
    dd = day_dir(year, day)

    # Create directory
    dd.mkdir(parents=True, exist_ok=True)

    # Scaffold part1.py and part2.py (skip if they already exist)
    for part in ["part1.py", "part2.py"]:
        part_path = dd / part
        if part_path.exists():
            print(
                f"  skip  {part_path.relative_to(get_project_root())} (already exists)"
            )
        else:
            part_path.write_text(SOLUTION_TEMPLATE)
            print(f"  create {part_path.relative_to(get_project_root())}")

    # Create empty test.txt if it doesn't exist
    test_path = dd / "test.txt"
    if not test_path.exists():
        test_path.write_text("")
        print(f"  create {test_path.relative_to(get_project_root())}")

    # Download input
    input_path = dd / "input.txt"
    if input_path.exists() and input_path.stat().st_size > 0:
        print(f"  skip  {input_path.relative_to(get_project_root())} (already exists)")
    else:
        _download_input(year, day, input_path)

    print(
        f"\nReady! Open {dd.relative_to(get_project_root())}/part1.py and start solving."
    )


def cmd_run(args: argparse.Namespace) -> None:
    """Run a solution with input.txt."""
    _run_solution(args.year, args.day, args.part, "input.txt")


def cmd_test(args: argparse.Namespace) -> None:
    """Run a solution with test.txt."""
    _run_solution(args.year, args.day, args.part, "test.txt")


def cmd_download(args: argparse.Namespace) -> None:
    """Bulk-download all available inputs for a year."""
    year = args.year
    now = datetime.now()

    # Figure out how many days are available
    if now.year > year or (now.year == year and now.month == 12 and now.day >= 25):
        max_day = 25
    elif now.year == year and now.month == 12:
        max_day = now.day
    elif now.year == year and now.month < 12:
        max_day = 0
    else:
        max_day = 25

    if max_day == 0:
        print(f"No puzzles available yet for {year}.")
        return

    print(f"Downloading inputs for {year} (days 1-{max_day})...")
    for day in range(1, max_day + 1):
        dd = day_dir(year, day)
        dd.mkdir(parents=True, exist_ok=True)
        input_path = dd / "input.txt"
        if input_path.exists() and input_path.stat().st_size > 0:
            print(f"  skip  day {day:02d} (already exists)")
        else:
            _download_input(year, day, input_path)
            time.sleep(0.5)  # Be polite to the server


def _download_input(year: int, day: int, dest: Path) -> None:
    """Download puzzle input using aocd."""
    try:
        from aocd import get_data

        data = get_data(day=day, year=year)
        dest.write_text(data)
        print(f"  download day {day:02d}")
    except ImportError:
        print(
            f"  skip  day {day:02d} (install advent-of-code-data: pip install advent-of-code-data)"
        )
    except Exception as e:
        print(f"  FAIL  day {day:02d}: {e}")
        # Create empty file so we don't crash later
        if not dest.exists():
            dest.write_text("")


def _run_solution(year: int, day: int, part: int, input_file: str) -> None:
    """Run a solution file, passing the input file as an argument."""
    dd = day_dir(year, day)
    script = dd / f"part{part}.py"

    if not script.exists():
        fallbacks = [
            dd / "solution.py",
            dd / f"part-{part}.py",
            dd / f"part_{part}.py",
            dd / f"aoc-{year}-{day:02d}.py",
            dd / f"day_{day}.py",
        ]
        for fb in fallbacks:
            if fb.exists():
                script = fb
                break
        else:
            print(f"No solution found at {script.relative_to(get_project_root())}")
            print(f"  (also checked: {', '.join(f.name for f in fallbacks)})")
            sys.exit(1)

    input_path = dd / input_file
    if not input_path.exists():
        print(f"Input file not found: {input_path.relative_to(get_project_root())}")
        sys.exit(1)

    # Run the solution from the day's directory (so relative paths work for old solutions)
    # Pass the input file as argv[1] (new solutions use it, old ones ignore it)
    result = subprocess.run(
        [sys.executable, script.name, input_file],
        cwd=dd,
        env={**os.environ, "PYTHONPATH": str(get_project_root())},
    )
    sys.exit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="aoc",
        description="Advent of Code project CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- new ---
    p_new = subparsers.add_parser("new", help="Scaffold a new day")
    p_new.add_argument("year", type=int)
    p_new.add_argument("day", type=int)
    p_new.set_defaults(func=cmd_new)

    # --- run ---
    p_run = subparsers.add_parser("run", help="Run a solution with input.txt")
    p_run.add_argument("year", type=int)
    p_run.add_argument("day", type=int)
    p_run.add_argument("part", type=int, choices=[1, 2])
    p_run.set_defaults(func=cmd_run)

    # --- test ---
    p_test = subparsers.add_parser("test", help="Run a solution with test.txt")
    p_test.add_argument("year", type=int)
    p_test.add_argument("day", type=int)
    p_test.add_argument("part", type=int, choices=[1, 2])
    p_test.set_defaults(func=cmd_test)

    # --- download ---
    p_dl = subparsers.add_parser("download", help="Bulk-download inputs for a year")
    p_dl.add_argument("year", type=int)
    p_dl.set_defaults(func=cmd_download)

    args = parser.parse_args()
    args.func(args)
