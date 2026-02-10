import math


def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        print(lines)
    return lines


def part_1(input):
    total = 0
    grid = []
    for line in input:
        grid.append(list(line))

    x_pos = 0
    y_pos = 0
    guard_dir = "^"

    # init guard position
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == guard_dir:
                x_pos = x
                y_pos = y

    positions = set()
    dir_order = ["^", ">", "v", "<"]
    dir_map = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    do_patrol = True

    while do_patrol:
        dir = dir_map.get(guard_dir)
        if not dir:
            break

        positions.add((x_pos, y_pos))

        next_x, next_y = x_pos + dir[0], y_pos + dir[1]

        print(f"x: {x_pos}, y: {y_pos}")
        print(f"next_x: {next_x}, next_y: {next_y}")
        print(f"guard_dir: {guard_dir}")
        print(f"dir: {dir}")

        if (
            next_x < 0
            or next_x > len(grid[next_y]) - 1
            or next_y < 0
            or next_y > len(grid) - 1
        ):
            break

        next_pos = grid[next_y][next_x]
        print(next_pos)

        if next_pos == "#":
            if guard_dir == "<":
                guard_dir = dir_order[0]
            else:
                new_index = dir_order.index(guard_dir) + 1
                guard_dir = dir_order[new_index]
            continue
        else:
            y_pos = next_y
            x_pos = next_x
    total = len(positions)

    return total


def point_dist(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def rect_check(pos, pos_hist):
    a = pos_hist[0]
    b = pos_hist[1]
    c = pos_hist[2]
    d = pos

    print(a, b, c, d)
    ab = point_dist(a, b)
    bc = point_dist(b, c)
    cd = point_dist(c, d)
    da = point_dist(d, a)

    if ab == cd and bc == da:
        print("RECTANGLE!")
        print(ab, bc, cd, da)
        return True

    return False


def part_2(input):
    total = 0
    grid = []
    for line in input:
        grid.append(list(line))

    x_pos = 0
    y_pos = 0
    guard_dir = "^"

    # init guard position
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == guard_dir:
                x_pos = x
                y_pos = y

    positions = set()
    turn_history = [(x_pos, y_pos)]
    dir_order = ["^", ">", "v", "<"]

    # invert up/down because list indexes
    dir_map = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    do_patrol = True

    while do_patrol:
        dir = dir_map.get(guard_dir)
        if not dir:
            break

        next_x, next_y = x_pos + dir[0], y_pos + dir[1]
        next_xy = (next_x, next_y)
        cur_xy = (x_pos, y_pos)

        if (
            next_x < 0
            or next_x > len(grid[next_y]) - 1
            or next_y < 0
            or next_y > len(grid) - 1
        ):
            break

        next_pos = grid[next_y][next_x]

        if next_pos == "#":
            if guard_dir == "<":
                guard_dir = dir_order[0]
            else:
                new_index = dir_order.index(guard_dir) + 1
                guard_dir = dir_order[new_index]
            turn_history.append((x_pos, y_pos))
            continue
        else:
            if len(turn_history) > 2:
                if rect_check(cur_xy, turn_history[-3:]) and next_xy != turn_history[0]:
                    positions.add(next_xy)

            y_pos = next_y
            x_pos = next_x
    total = len(positions)

    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
