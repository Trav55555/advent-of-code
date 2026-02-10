def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        # print(lines)
    return lines


def part_1(input):
    total = 0

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == "X":
                total += xmas_word_search(i, j, input)
    return total


def xmas_word_search(i, j, lines):
    match_count = 0
    word = "XMAS"
    word_len = 4
    total_lines = len(lines)
    line_len = len(lines[i])

    x = [-1, -1, -1, 0, 0, 1, 1, 1]  # x search direction
    y = [-1, 0, 1, -1, 1, -1, 0, 1]  # y search direction

    for dir in range(8):
        cur_x, cur_y = j + x[dir], i + y[dir]
        k = 1

        while k < word_len:
            # break if out of bounds
            if cur_x >= line_len or cur_x < 0 or cur_y >= total_lines or cur_y < 0:
                break

            # break if not match
            if lines[cur_y][cur_x] != word[k]:
                break

            cur_x += x[dir]
            cur_y += y[dir]
            k += 1

        if k == word_len:
            match_count += 1
    return match_count


def mas_x_search(i, j, lines):
    match_count = 0
    words = ["MAS", "SAM"]
    total_lines = len(lines)
    line_len = len(lines[i])

    x = [-1, 1, -1, 1]  # x search direction
    y = [-1, 1, 1, -1]  # y search direction
    d = ["", "", "", ""]

    for dir in range(4):
        cur_x, cur_y = j + x[dir], i + y[dir]
        if cur_x >= line_len or cur_x < 0 or cur_y >= total_lines or cur_y < 0:
            break
        d[dir] = lines[cur_y][cur_x]

    d1 = "".join([d[0], lines[i][j], d[1]])
    d2 = "".join([d[2], lines[i][j], d[3]])

    if d1 in words and d2 in words:
        print(d1, d2)
        match_count += 1

    return match_count


def part_2(input):
    total = 0

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char == "A":
                total += mas_x_search(i, j, input)

    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
