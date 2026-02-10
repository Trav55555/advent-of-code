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

    time = ''.join(times)
    distance = ''.join(distances)

    print(f'distance: {distance}')
    print(f'time: {time}')


    winning_times = []
    result_map = {}
    record_distance = int(distance)
    race_time = int(time)

    for i in range(race_time):
        distance = calculate_distance(i, race_time)
        if distance > record_distance:
            winning_times.append(i)
        print(f'{i}: {distance}')

    print(len(winning_times))
