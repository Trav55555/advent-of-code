def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


def calculate_distance(charge_time, race_time):
    running_time = race_time - charge_time
    speed = charge_time
    return running_time * speed


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")

    for line in input_data:
        print(line)
        if "Time:" in line:
            times = line.split("Time:")[1].strip().split(" ")
            times = [time for time in times if time != ""]
        if "Distance:" in line:
            distances = line.split("Distance:")[1].strip().split(" ")
            distances = [distance for distance in distances if distance != ""]
    
    input_map = {}
    for t, d in zip(times, distances):
        input_map[t] = d

    print(input_map)

    total_wins = []

    for key in input_map:
        winning_times = []
        result_map = {}
        record_distance = int(input_map[key])
        race_time = int(key)

        for i in range(int(key)):
            distance = calculate_distance(i, race_time)
            if distance > record_distance:
                winning_times.append(i)

        total_wins.append(len(winning_times))

    win_total = 1 
    for wins in total_wins:
        win_total *= wins
    
    print(win_total)