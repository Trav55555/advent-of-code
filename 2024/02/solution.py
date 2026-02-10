def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        # print(lines)
    return lines


def validate_report(report):
    is_safe = True
    prev_x = ""
    next_x = ""

    for i, x in enumerate(report):
        report_len = len(report)

        if i != 0:
            prev_x = report[i - 1]

        if i < report_len - 1:
            next_x = report[i + 1]
        else:
            next_x = ""

        if prev_x:
            if abs(x - prev_x) > 3:
                is_safe = False

        if next_x:
            # print(f"prev_x: {type(prev_x)}, x: {type(x)}, next_x: {type(next_x)}")
            if abs(x - next_x) > 3:
                is_safe = False

        if prev_x and next_x:
            if prev_x < x < next_x:
                pass
            elif prev_x > x > next_x:
                pass
            else:
                is_safe = False

        if not is_safe:
            break

    return is_safe


def part_1(input):
    total = 0

    reports = [report.split() for report in input]

    for report in reports:
        report = [int(x) for x in report]
        if validate_report(report):
            total += 1

    return total


def part_2(input):
    total = 0
    is_safe = True
    reports = [report.split() for report in input]

    for report in reports:
        report = [int(x) for x in report]
        is_safe = validate_report(report)

        if not is_safe:
            for i, level in enumerate(report):
                new_report = report.copy()
                new_report.pop(i)
                if validate_report(new_report):
                    is_safe = True

        if is_safe:
            total += 1

    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
