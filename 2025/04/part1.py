"""Parses the grid into a set of coordinate tuples, then iteratively identifies and removes accessible rolls layer-by-layer until no accessible rolls remain."""


def get_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f]
    return lines


def main():
    paper_grid = get_input("input.txt")
    roll_coords = set()

    for i, row in enumerate(paper_grid):
        for j, col in enumerate(row):
            if col == "@":
                roll_coords.add((j, i))

    accessible_rolls = set()
    for x, y in roll_coords:
            neighbors = sum(
                (x + dx, y + dy) in roll_coords
                for dx in (-1, 0, 1)
                for dy in (-1, 0, 1)
                if (dx, dy) != (0, 0)
            )
            if neighbors < 4:
                accessible_rolls.add((x, y))

    print(len(accessible_rolls))

if __name__ == "__main__":
    main()
