"""Since overlapping beams represent distinct timelines, use a Dictionary (or hash map) to sum the total path counts at each position."""

from collections import defaultdict


def get_input(input_file):
    with open(input_file, "r") as f:
        input = f.read().strip().split("\n")
    return input


def main():
    grid = get_input("input.txt")

    h = len(grid)
    w = len(grid[0])

    start_col = 0
    for c in range(w):
        if grid[0][c] == "S":
            start_col = c
            break

    current_beams = defaultdict(int)
    current_beams[start_col] = 1

    total_finished_timelines = 0

    for r in range(h):
        next_beams = defaultdict(int)

        for c, count in current_beams.items():
            char = grid[r][c]

            if char == "S" or char == ".":
                next_beams[c] += count
            elif char == "^":
                if c - 1 >= 0:
                    next_beams[c - 1] += count
                else:
                    total_finished_timelines += count

                if c + 1 < w:
                    next_beams[c + 1] += count
                else:
                    total_finished_timelines += count
        current_beams = next_beams

    total_finished_timelines += sum(current_beams.values())
    print(total_finished_timelines)


if __name__ == "__main__":
    main()
