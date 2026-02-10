import re


def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        print(lines)
    return lines


def part_1(input):
    total = 0

    mul_regex = r"(mul\([0-9]+,[0-9]+\))"

    matches = []
    for line in input:
        matches.extend(re.findall(mul_regex, line))
    print(matches)
    print(len(matches))

    mul_list = [mul.strip("mul(").strip(")").split(",") for mul in matches]
    print(mul_list)
    for mul in mul_list:
        total += int(mul[0]) * int(mul[1])

    return total


def part_2(input):
    total = 0
    do_math = True

    new_regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    matches = []
    for line in input:
        matches.extend(re.findall(new_regex, line))

    print(matches)
    print(len(matches))

    for m in matches:
        if m == "do()":
            do_math = True
        elif m == "don't()":
            do_math = False
        elif do_math:
            print(m)
            mul = m.strip("mul(").strip(")").split(",")
            print(mul)
            total += int(mul[0]) * int(mul[1])

    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
