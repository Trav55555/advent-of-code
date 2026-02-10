def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


def check_gear(index, line_map):
    gear_ratio = 0
    gear_valid = False

    part_numbers = []

    for key in line_map.keys():
        if line_map[key]:
            start = index
            end = index
            if index > 0:
                start = index - 1
            if index < len(line) - 1:
                end = index + 1

            for i in range(start, end + 1):
                if line_map[key][i].isdigit():
                    part_number = get_whole_part_number(i, line_map[key])
                    if not part_numbers:
                        part_numbers.append(part_number)
                    if part_number != part_numbers[-1]:
                        part_numbers.append(part_number)
    print(part_numbers)
    if len(part_numbers) == 2:
        gear_ratio = int(part_numbers[0]) * int(part_numbers[1])
        print(f'Gear ratio: {gear_ratio}')
        gear_valid = True

    return {
        'valid': gear_valid,
        'ratio': gear_ratio
    }


def get_whole_part_number(index, line):
    search_right = True
    search_left = True
    part_number = [line[index]]
    right_index = index
    left_index = index

    while search_right:
        if right_index < len(line) - 1:
            if line[right_index + 1].isdigit():
                part_number.append(line[right_index + 1])
                right_index += 1
            else:
                search_right = False
        else:
            search_right = False

    while search_left:
        if left_index > 0:
            if line[left_index - 1].isdigit():
                part_number.insert(0, line[left_index - 1])
                left_index -= 1
            else:
                search_left = False
        else:
            search_left = False

    return "".join(part_number)


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")

    gear_ratio_sum = 0

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

        for j, char in enumerate(line):
            if char == '*':
                gear_check_result = check_gear(j, line_map)
                if gear_check_result.get('valid'):
                    gear_ratio_sum += gear_check_result.get('ratio')

    print(gear_ratio_sum)
