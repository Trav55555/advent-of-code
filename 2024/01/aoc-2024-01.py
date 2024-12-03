def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        print(lines)
    return lines


def part_1(input):
    left_list = []
    right_list = []
    total = 0

    for line in input:
        split_line = line.split()
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1]))

    while left_list and right_list:
        left_min = min(left_list)
        right_min = min(right_list)
        distance = abs(left_min - right_min)
        total += distance
        left_list.remove(left_min)
        right_list.remove(right_min)

    print(left_list)
    print(right_list)

    return total


def part_2(input):
    left_list = []
    right_list = []
    total = 0

    for line in input:
        split_line = line.split()
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1]))

    count_cache = {}
    for x in left_list:
        if x not in count_cache:
            count_cache[x] = right_list.count(x)
        total += x * count_cache[x]

    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
