

def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt")

    cal_total = 0

    number_word_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    starting_letters = set([key[0] for key in number_word_map.keys()])
    print(starting_letters)

    for line in input_data.split("\n"):
        cal_value = ''

        for i, char in enumerate(line):
            if char.isdigit():
                cal_value += char
            elif char in starting_letters:
                slice_of_line = line[i:i+5]
                for key in number_word_map:
                    if key in slice_of_line:
                        add_to_cal_value = True
                        for j, key_char in enumerate(key):
                            if line[i+j] != key_char:
                                add_to_cal_value = False
                                break
                        if add_to_cal_value:
                            cal_value += number_word_map[key]

        first_char = cal_value[0]
        last_char = cal_value[-1]

        cal_total += int(first_char + last_char)

    print(cal_total)
