def read_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def main():
    count = 0
    virtual_pos = 50

    # left is negative, right is positive
    turns = read_input("input.txt")
    for turn in turns:
        if not turn:
            continue

        direction = turn[0]
        num = int(turn[1:])

        if direction == "R":
            prev_pos = virtual_pos
            virtual_pos += num

            crossings = (virtual_pos // 100) - (prev_pos // 100)
            count += crossings

        elif direction == "L":
            prev_pos = virtual_pos
            virtual_pos -= num

            crossings = ((prev_pos - 1) // 100) - ((virtual_pos - 1) // 100)
            count += crossings
    print(count)


if __name__ == "__main__":
    main()
