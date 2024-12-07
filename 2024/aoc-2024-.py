def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        print(lines)
    return lines


def part_1(input):
    return ""


def part_2(input):
    return ""


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
