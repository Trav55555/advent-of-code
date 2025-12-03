def read_input(file):
    with open(file, "r") as f:
        return f.read().splitlines()


def main():
    count = 0
    current_pos = 50
    dir = 1
    # left is negative, right is positive
    turns = read_input("input.txt")
    for turn in turns:
        if turn:
            if turn[0] == "R":
                dir = 1
            if turn[0] == "L":
                dir = -1
            num = int(turn[1:])
            current_pos = (current_pos + dir * num) % 100
            if current_pos == 0:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
