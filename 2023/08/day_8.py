def part_1(input):
    camel_path = input[0]
    node_list = input[1].split("\n")
    print(node_list)
    path_map = {"L": 0, "R": 1}

    node_map = {}

    for node in node_list:
        print(f"node: {node}")
        node_split = node.split(" = ")
        key = node_split[0]
        value = node_split[-1].replace("(", "").replace(")", "").split(", ")

        node_map[key] = (value[0], value[1])

    print(node_map)

    node = "AAA"
    steps = 0
    print(f"{steps}: {node}")

    while node != "ZZZ":
        for char in camel_path:
            steps += 1
            next_node = node_map[node][path_map[char]]
            print(f"{steps}: {next_node}")
            node = next_node


def part_2(input):
    camel_path = input[0]
    node_list = input[1].split("\n")

    path_map = {"L": 0, "R": 1}

    node_map = {}

    starting_nodes = []

    for node in node_list:
        print(f"node: {node}")
        node_split = node.split(" = ")
        key = node_split[0]
        value = node_split[-1].replace("(", "").replace(")", "").split(", ")

        if key[-1] == "A":
            starting_nodes.append(key)

        node_map[key] = (value[0], value[1])

    print(starting_nodes)

    nodes = starting_nodes.copy()
    steps = 0

    # brute force not effective here, need to use LCM bc loops are cyclical
    while True:
        for char in camel_path:
            # print(nodes)
            steps += 1
            # print(steps)
            for i, node in enumerate(nodes):
                next_node = node_map[node][path_map[char]]
                # print(f"{steps}: {next_node}")
                nodes[i] = next_node
            node_ends = [node[-1] for node in nodes]
            print(f"{steps}: {node_ends}")
            if all(node_ends) == "Z":
                break


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.read().split("\n\n")

    part_1(input_data)

    part_2(input_data)
