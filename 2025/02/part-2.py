"""We generate the set of all possible matches, then check against the ranges"""


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

    candidates = set()

    for length in range(1, max_half + 1):
        start = 10 ** (length - 1)
        end = 10**length

        for i in range(start, end):
            s = str(i)

            k = 2
            while True:
                candidate_str = s * k
                if len(candidate_str) > max_digits:
                    break

                val = int(candidate_str)

                if val > max:
                    break

                candidates.add(val)
                k += 1

    total = 0
    sorted_candidates = sorted(list(candidates))

    for val in sorted_candidates:
        for start, end in ranges:
            if start <= val <= end:
                total += val
                break

    print(total)


if __name__ == "__main__":
    main()
