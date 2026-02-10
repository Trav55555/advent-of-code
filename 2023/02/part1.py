def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt")

    elf_map = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    game_map = {}

    id_sum = 0

    for line in input_data.split("\n"):
        game_id = line.split(":")[0].split(" ")[-1]
        pulls = line.split(": ")[1].split(";")
        parsed_pulls = []

        for pull in pulls:
            parsed_pull = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }

            pull_split = pull.split(",")
            for cube_set in pull_split:
                cube_set = cube_set.strip()
                color = cube_set.split(" ")[-1]
                amount = int(cube_set.split(" ")[0])

                parsed_pull[color] += amount

            parsed_pulls.append(parsed_pull)

        game_map[game_id] = parsed_pulls

    for game in game_map:
        is_valid = True
        for pull in game_map[game]:
            for color in pull:
                if pull[color] > elf_map[color]:
                    is_valid = False
                    break
        if is_valid:
            id_sum += int(game)

    print(id_sum)
