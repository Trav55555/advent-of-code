def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")

    point_sum = 0 

    cards = {}

    for line in input_data:
        split_line = line.split(":") 
        card_id = split_line[0].split(" ")[-1]

        numbers = split_line[1].strip().split("|")

        winning_numbers = numbers[0].strip().split(" ")

        played_numbers = numbers[-1].strip().split(" ")

        winning_numbers = list(filter(None, winning_numbers))
        played_numbers = list(filter(None, played_numbers))

        card_wins = 0
        card_value = 0

        for x in played_numbers:
            if x in winning_numbers:
                card_wins += 1
        
        if card_wins > 0:
            card_value = 2 ** (card_wins - 1)

        cards[card_id] = {
            "winning_numbers": winning_numbers,
            "played_numbers": played_numbers,
            "card_wins": card_wins,
            "card_value": card_value
        }
        print(cards[card_id])
        point_sum += card_value
    
    print(point_sum)
