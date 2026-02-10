"""Sort the list of ranges, merge overlaps, then count unique numbers in ranges"""


def get_input(input_file):
    ranges = []
    ids = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            n_line = [int(x) for x in line.split("-")]

            if len(n_line) == 2:
                ranges.append(n_line)
            elif len(n_line) == 1:
                ids.append(n_line[0])

    ranges.sort()
    ids.sort()

    return ranges, ids


def main():
    fresh_total = 0

    ranges, ids = get_input("input.txt")

    x, y = ranges[0]
    merged = []
    for i in range(1, len(ranges)):
        next_x, next_y = ranges[i]

        if next_x <= y:
            y = max(y, next_y)
        else:
            merged.append((x, y))
            x, y = next_x, next_y

    merged.append((x, y))

    fresh_total = sum((y - x + 1) for x, y in merged)

    print(fresh_total)


if __name__ == "__main__":
    main()
