

def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt")

    cal_total = 0

    for line in input_data.split("\n"):
        cal_value = ''
        for char in line:
            if char.isdigit():
                cal_value += char

        first_char = cal_value[0]
        last_char = cal_value[-1]
        cal_total += int(first_char + last_char)

    print(cal_total)
