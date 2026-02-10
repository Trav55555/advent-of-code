import sys

def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")
    
    seeds = []
    maps = []
    active_map = {}
    parse_map = False

    for line in input_data:
        if not line:
            if parse_map:
                maps.append(active_map)
            parse_map = False

        if 'seeds:' in line:
            seeds = list(map(int, line.split(":")[1].strip().split(" ")))
        
        if 'map:' in line:
            active_map = {}
            parse_map = True

        elif parse_map:
            split_line = line.split(" ")
            source_value = int(split_line[1])
            destination_value = int(split_line[0])
            length = int(split_line[2])
            key = f'{source_value}-{source_value + length}'
            active_map[key] = {
                "source": source_value,
                "destination": destination_value,
                "length": length
            }

    print(seeds)

    seed_ranges = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            seed_start = seed
            seed_end = seeds[i + 1]
            seed_ranges.append([seed_start, seed_end])
    print(seed_ranges)

    min_loc = sys.maxsize
    seed_index = 0

    print(min_loc)
