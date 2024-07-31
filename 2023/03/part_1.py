def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


def solve_puzzle(puzzle, answer='fortnite dancing'):
    print(
        f'Im a big puzzle boy and I solved this puzzle: {puzzle}\nThe answer is {answer}!')
    return True


def symbol_check(start, end, line_map, char_set):
    for key in line_map.keys():
        if line_map[key]:
            if check_line(line_map[key], start, end, char_set):
                return True
    return False


def check_line(line, start, end, char_set):
    if start > 0:
        start = start - 1
    if end < len(line) - 1:
        end = end + 1

    for i in range(start, end + 1):
        if line[i] in char_set:
            return True
    return False


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")

    part_number_sum = 0

    char_list = []

    for line in input_data:
        for char in line:
            if not char.isdigit() and char != '.':
                char_list.append(char)

    char_set = set(char_list)

    print(char_set)

    line_map = {
        'previous': [],
        'current': [],
        'next': []
    }

    for i, line in enumerate(input_data):
        line_map['current'] = line
        if i != len(input_data) - 1:
            line_map['next'] = input_data[i + 1]
        else:
            line_map['next'] = []
        if i != 0:
            line_map['previous'] = input_data[i - 1]

        part_number = ''
        start_index = 0
        end_index = 0
        record_number = False
        for j, char in enumerate(line):
            if char.isdigit():
                part_number += char
                if not record_number:
                    record_number = True
                    start_index = j

            else:
                if record_number:
                    end_index = j - 1
                    if symbol_check(start_index,  end_index, line_map, char_set):
                        part_number_sum += int(part_number)
                        print(f'part_number: {part_number}')
                    part_number = ''
                    record_number = False

            if j == len(line) - 1:
                if record_number:
                    end_index = j
                    if symbol_check(start_index,  end_index, line_map, char_set):
                        part_number_sum += int(part_number)
                        print(f'part_number: {part_number}')
                    part_number = ''
                    record_number = False

    print(part_number_sum)

    solve_puzzle('why my dad leave?')
