def part_1(input):
    total_sum = 0
    for sequence in input:
        differences = [sequence]

        while True:
            # print(sequence)
            if all(x == 0 for x in sequence):
                break
            diff = []
            e = len(sequence)
            for i in range(e):
                if 0 < i < e:
                    diff.append(sequence[i] - sequence[i - 1])
            differences.append(diff)
            sequence = diff

        diff_len = len(differences)
        next_val = 0

        differences.reverse()

        # print(f"diff_len: {diff_len}")
        for i in range(diff_len):
            # print(f"i: {i}")
            sequence = differences[i]
            sequence.append(next_val)
            if i < (diff_len - 1):
                next_sequence = differences[i + 1]
                next_val = sequence[-1] + next_sequence[-1]

        total_sum += next_val

    print(total_sum)


def part_2(input):
    total_sum = 0
    for sequence in input:
        differences = [sequence]

        while True:
            print(sequence)
            if all(x == 0 for x in sequence):
                break
            diff = []
            e = len(sequence)
            for i in range(e):
                if 0 < i < e:
                    diff.append(sequence[i] - sequence[i - 1])
            differences.append(diff)
            sequence = diff

        diff_len = len(differences)
        next_val = 0

        differences.reverse()

        print(f"diff_len: {diff_len}")
        for i in range(diff_len):
            print(f"i: {i}")
            sequence = differences[i]
            sequence.insert(0, next_val)
            if i < (diff_len - 1):
                next_sequence = differences[i + 1]
                next_val = next_sequence[0] - sequence[0]

        total_sum += next_val

    print(total_sum)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read().split("\n")

        sequences = [[int(x) for x in seq.split(" ")] for seq in data]

    part_1(sequences)

    part_2(sequences)
