"""for each battery bank, find the biggest digit that isn't the last, then search again from the index after that one."""


def read_input(input_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
        return lines


def main():
    banks = read_input("input.txt")
    total = 0

    for bank in banks:
        first_index = 0
        first_val = 0
        second_val = 0
        for i, n in enumerate(bank):
            if i == len(bank) - 1:
                break
            if int(n) > first_val:
                first_index = i
                first_val = int(n)

        for i, n in enumerate(bank[first_index + 1 :]):
            if int(n) > second_val:
                second_val = int(n)

        joltage = str(first_val) + str(second_val)
        total += int(joltage)
    print(total)


if __name__ == "__main__":
    main()
