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

    current_beams = {start_col}
    total_splits = 0

    for r in range(h):
        next_beams = set()

        for c in current_beams:
            if c < 0 or c >= w:
                continue

            char = grid[r][c]

            if char == "S" or char == ".":
                next_beams.add(c)
            elif char == "^":
                total_splits += 1
                next_beams.add(c - 1)
                next_beams.add(c + 1)

        current_beams = next_beams

        if not current_beams:
            break
    print(total_splits)


if __name__ == "__main__":
    main()
