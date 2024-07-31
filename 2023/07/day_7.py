from collections import Counter
from functools import cmp_to_key

HAND_TYPES = {
    "FIVE_OF_A_KIND": 7,
    "FOUR_OF_A_KIND": 6,
    "FULL_HOUSE": 5,
    "THREE_OF_A_KIND": 4,
    "TWO_PAIR": 3,
    "ONE_PAIR": 2,
    "HIGH_CARD": 1,
}


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


def get_hand_type(hand, j_mode):
    if j_mode:
        j_count = hand.count("J")
        hand = [c for c in hand if c != "J"]
    else:
        j_count = 0

    hand_counts = Counter(hand).most_common(2)

    if len(hand_counts) > 0:
        first_place = hand_counts[0][1]
    else:
        first_place = 0

    if len(hand_counts) > 1:
        second_place = hand_counts[1][1]
    else:
        second_place = 0

    match first_place + j_count:
        case 5:
            return "FIVE_OF_A_KIND"

        case 4:
            return "FOUR_OF_A_KIND"

        case 3:
            match second_place:
                case 2:
                    return "FULL_HOUSE"
                case _:
                    return "THREE_OF_A_KIND"
        case 2:
            match second_place:
                case 2:
                    return "TWO_PAIR"
                case _:
                    return "ONE_PAIR"
        case _:
            return "HIGH_CARD"


def compare_1(a, b):
    cards = "23456789TJQKA"
    type_a = HAND_TYPES[a.get("hand_type")]
    type_b = HAND_TYPES[b.get("hand_type")]

    if type_a > type_b:
        return 1
    elif type_a < type_b:
        return -1
    for card_a, card_b in zip(a.get("cards"), b.get("cards")):
        if card_a == card_b:
            continue
        a_wins = cards.index(card_a) > cards.index(card_b)
        return 1 if a_wins else -1


def compare_2(a, b):
    cards = "J23456789TQKA"
    type_a = HAND_TYPES[a.get("hand_type")]
    type_b = HAND_TYPES[b.get("hand_type")]

    if type_a > type_b:
        return 1
    elif type_a < type_b:
        return -1
    for card_a, card_b in zip(a.get("cards"), b.get("cards")):
        if card_a == card_b:
            continue
        a_wins = cards.index(card_a) > cards.index(card_b)
        return 1 if a_wins else -1


def part_1(input_data):
    hands = []
    j_mode = False
    for line in input_data:
        split_line = line.split(" ")
        hands.append(
            {
                "cards": split_line[0],
                "bid": int(split_line[1]),
                "hand_type": get_hand_type(split_line[0], j_mode),
            }
        )

    hands.sort(key=cmp_to_key(compare_1))

    total = 0
    for rank, hand in enumerate(hands, start=1):
        total += rank * hand.get("bid")
    print(f"part_1 total: {total}")


def part_2(input_data):
    hands = []
    j_mode = True
    for line in input_data:
        split_line = line.split(" ")
        hands.append(
            {
                "cards": split_line[0],
                "bid": int(split_line[1]),
                "hand_type": get_hand_type(split_line[0], j_mode),
            }
        )

    hands.sort(key=cmp_to_key(compare_2))

    total = 0
    for rank, hand in enumerate(hands, start=1):
        total += rank * hand.get("bid")
    print(f"part_2 total: {total}")


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")
    part_1(input_data)
    part_2(input_data)
