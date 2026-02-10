def read_input(input_file):
    with open(input_file, "r") as f:
        content = f.read().strip()
        input_list = content.split(",")
        print(input_list)
        return input_list


def main():
    input = read_input("input.txt")
    ranges = [list(map(int, i.split("-"))) for i in input]
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    max = sorted_ranges[-1][-1]
    max_digits = len(str(max))
    max_half = (max_digits // 2) + 1

    candidates = []

    for length in range(1, max_half + 1):
        start = 10 ** (length - 1)
        end = 10**length

        for i in range(start, end):
            s = str(i)
            doubled_s = int(s + s)
            if doubled_s > max:
                break
            candidates.append(doubled_s)

    invalid_ids = set()

    for val in candidates:
        for start, end in ranges:
            if start <= val <= end:
                invalid_ids.add(val)
                break

    total = sum(invalid_ids)
    print(total)


if __name__ == "__main__":
    main()
