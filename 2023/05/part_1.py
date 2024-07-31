def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


def get_location(seed, map_map):
    source = int(seed)
    dest = 0
    for key in map_map.keys():
        source_mapped = False
        # print(f'{map_map[key]["source"]} --> {map_map[key]["destination"]}')
        for entry_key in map_map[key]["entries"].keys():
            key_range = entry_key.split("-")
            if int(key_range[0]) <= source <= int(key_range[1]):
                source_diff = source - int(key_range[0])
                dest = int(map_map[key]["entries"][entry_key]["destination"]) + source_diff
                source = dest
                source_mapped = True
                break 
        if not source_mapped:
            dest = source
    return dest
       

if __name__ == "__main__":
    input_data = read_input("input.txt").split("\n")
    
    seeds = []

    map_map = {}

    parse_map = False
    for line in input_data:
        if not line:
            parse_map = False

        if 'seeds:' in line:
            split_line = line.split(":")
            seeds = split_line[1].strip().split(" ")
        
        if 'map:' in line:
            parse_map = True
            split_line = line.split(" ")
            map_name = split_line[0]
            source = map_name.split("-")[0]
            destination = map_name.split("-")[2]
            map_map[map_name] = {
                "source": source,
                "destination": destination,
                "entries": {}
            }

        elif parse_map:
            split_line = line.split(" ")
            source_value = split_line[1]
            destination_value = split_line[0]
            length = split_line[2]
            entry_key = f'{source_value}-{int(source_value) + int(length)}'
            map_map[map_name]["entries"][entry_key] = {
                "source": source_value,
                "destination": destination_value,
                "length": length
            }
                

    min_loc = ''
    for seed in seeds:
        print(f'Processing seed: {seed}')
        location = get_location(seed, map_map)
        if not min_loc:
            min_loc = location
        elif location < min_loc:
            min_loc = location
    
    print(map_map)
    print(min_loc)
