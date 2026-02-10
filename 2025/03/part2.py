"This uses a greedy approach: it finds the largest possible digit within the available range, locks it in, and advances past it, repeating until 12 digits are found."


def read_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        return lines


def solve_bank(bank):
    digits = 12
    start_index = 0
    result_digits = []

    for i in range(digits):
        remaining_digits = digits - (i + 1)

        if remaining_digits > 0:
            search_window = bank[start_index:-remaining_digits]
        else:
            search_window = bank[start_index:]

        best_digit = max(search_window)

        result_digits.append(best_digit)

        relative_index = search_window.index(best_digit)

        start_index += relative_index + 1
    return int("".join(result_digits))


def main():
    banks = read_input("input.txt")
    total = 0

    for bank in banks:
        total += solve_bank(bank)
    print(total)


if __name__ == "__main__":
    main()
