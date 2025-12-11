from math import prod


def get_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip("\n") for line in f]
    return lines


def main():
    lines = get_input("input.txt")

    max_width = max(len(line) for line in lines)
    grid = [line.ljust(max_width) for line in lines]

    grand_total = 0

    current_problem_nums = []
    current_operator = None

    for x in range(max_width - 1, -1, -1):
        col_chars = [row[x] for row in grid]

        digits = []
        found_symbol_in_col = None

        for char in col_chars:
            if char.isdigit():
                digits.append(char)
            elif char in "+*":
                found_symbol_in_col = char

        is_empty_column = len(digits) == 0 and found_symbol_in_col is None

        if not is_empty_column:
            if digits:
                number = int("".join(digits))
                current_problem_nums.append(number)

            if found_symbol_in_col:
                current_operator = found_symbol_in_col

        else:
            if current_problem_nums:
                if current_operator == "+":
                    grand_total += sum(current_problem_nums)
                elif current_operator == "*":
                    grand_total += prod(current_problem_nums)

                current_problem_nums = []
                current_operator = None

    if current_problem_nums:
        if current_operator == "+":
            grand_total += sum(current_problem_nums)
        elif current_operator == "*":
            grand_total += prod(current_problem_nums)

    print(grand_total)


if __name__ == "__main__":
    main()
