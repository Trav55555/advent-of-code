"""Solution file template used by the CLI scaffolder."""

SOLUTION_TEMPLATE = """\
import sys
from pathlib import Path

# Add project root to path so helpers can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from helpers.reader import read_lines


def solve(lines):
    total = 0
    return total


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    print(solve(read_lines(input_file)))
"""
