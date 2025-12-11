"""Rotate the lists, then parse and sum or prod all but the last char"""

from math import prod


def get_input(input_file):
    with open(input_file, "r") as f:
        lines = []
        for line in f:
            line = line.strip().split()
            lines.append(line)

    return lines


def main():
    total = 0
    lines = get_input("input.txt")
    rotated_lines = {}
    for i in lines:
        for j in range(len(i)):
            if rotated_lines.get(j):
                rotated_lines[j].append(i[j])
            else:
                rotated_lines[j] = [i[j]]
    for i, line in rotated_lines.items():
        if line[-1] == "+":
            total += sum(int(x) for x in line[:-1])
        elif line[-1] == "*":
            total += prod(int(x) for x in line[:-1])
    print(total)


if __name__ == "__main__":
    main()
