"""sort the ranges and ids, check if id is in any range, if yes increment."""


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

    for i in ids:
        for rx, ry in ranges:
            if rx <= i <= ry:
                fresh_total += 1
                break

    print(fresh_total)


if __name__ == "__main__":
    main()
