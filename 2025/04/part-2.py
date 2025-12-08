"""Parses the grid into a set of coordinate tuples, then iteratively identifies and removes accessible rolls layer-by-layer until no accessible rolls remain."""


def get_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f]
    return lines


def main():
    total = 0

    paper_grid = get_input("input.txt")
    roll_coords = set()

    count = 0
    for i, row in enumerate(paper_grid):
        for j, col in enumerate(row):
            if col == "@":
                count += 1
                roll_coords.add((j, i))

    while True:
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
        if not accessible_rolls:
            break

        total += len(accessible_rolls)
        roll_coords -= accessible_rolls

    print(f"Removed {total} of {count}")


if __name__ == "__main__":
    main()
