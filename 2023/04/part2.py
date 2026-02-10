def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")

    cards = {}

    copies = {}


    # populate initial card dictionary
    for line in input_data:
        split_line = line.split(":") 
        card_id = split_line[0].split(" ")[-1]

        numbers = split_line[1].strip().split("|")

        winning_numbers = numbers[0].strip().split(" ")

        played_numbers = numbers[-1].strip().split(" ")

        winning_numbers = list(filter(None, winning_numbers))
        played_numbers = list(filter(None, played_numbers))

        card_wins = 0

        for x in played_numbers:
            if x in winning_numbers:
                card_wins += 1
        
        cards[card_id] = {
            "winning_numbers": winning_numbers,
            "played_numbers": played_numbers,
            "card_wins": card_wins
        }

        copies[card_id] = 1

    # iterate through cards and apply copy rules
    for card_id in cards.keys():
        wins = cards[card_id]["card_wins"]
        for copy in range(copies[card_id]):
            for x in range(int(card_id), (int(card_id) + wins + 1)):
                if x > int(card_id):
                    copies[str(x)] += 1

    total_copies = 0

    for key in copies.keys():
        total_copies += copies[key]        
    
    print(total_copies)

