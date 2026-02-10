def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt")

    game_map = {}

    power_sum = 0

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
        color_max = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for pull in game_map[game]:
            for color in pull:
                if pull[color] > color_max[color]:
                    color_max[color] = pull[color]

        power_sum += color_max['red'] * color_max['green'] * color_max['blue']

    print(power_sum)
