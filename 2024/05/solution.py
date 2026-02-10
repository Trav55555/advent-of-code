def read_input():
    file = "./input.txt"
    with open(file) as f:
        lines = [line.rstrip("\n") for line in f]
        print(lines)
    return lines


def part_1(input):
    total = 0
    rules = {}
    update_list = []
    for line in input:
        if "|" in line:
            split_line = line.split("|")
            num_1 = split_line[0]
            num_2 = split_line[1]
            if num_1 not in rules:
                rules[num_1] = []
            if num_2 not in rules[num_1]:
                rules[num_1].append(num_2)
        elif line:
            update_list.append(line.split(","))

    for update in update_list:
        is_valid = True
        for i, page in enumerate(update):
            if i > 0:
                page_rules = rules.get(page)
                if page_rules:
                    for j, rule_check in enumerate(update):
                        if j == i:
                            break
                        if rule_check in page_rules:
                            is_valid = False
                            break
            if not is_valid:
                break
        if is_valid:
            middle = int(update[int((len(update) - 1) / 2)])
            total += middle

    return total


def check_valid(rules, update):
    is_valid = True
    i = ""
    j = ""
    for i, page in enumerate(update):
        if i > 0:
            page_rules = rules.get(page)
            if page_rules:
                for j, rule_check in enumerate(update):
                    if j == i:
                        break
                    if rule_check in page_rules:
                        print(f"rule_check: {rule_check}")
                        is_valid = False
                        break
        if not is_valid:
            break
    print(f"is_valid: {is_valid}")
    return is_valid, i, j


def part_2(input):
    total = 0
    rules = {}
    update_list = []
    for line in input:
        if "|" in line:
            split_line = line.split("|")
            num_1 = split_line[0]
            num_2 = split_line[1]
            if num_1 not in rules:
                rules[num_1] = []
            if num_2 not in rules[num_1]:
                rules[num_1].append(num_2)
        elif line:
            update_list.append(line.split(","))

    for update in update_list:
        sum_middle = False
        is_valid, i, j = check_valid(rules, update)

        while not is_valid:
            sum_middle = True
            print(f"update: {update}")
            print(i, j)
            print(rules[update[i]])
            print(update[i], print(update[j]))
            update[i], update[j] = update[j], update[i]
            is_valid, i, j = check_valid(rules, update)
        if sum_middle:
            middle = int(update[int((len(update) - 1) / 2)])
            total += middle
    return total


if __name__ == "__main__":
    input = read_input()

    print(part_1(input))

    print(part_2(input))
