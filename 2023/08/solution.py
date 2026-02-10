from math import lcm
from functools import reduce


def part_1(input):
    camel_path = input[0]
    node_list = input[1].split("\n")

    path_map = {"L": 0, "R": 1}

    node_map = {}

    for node in node_list:
        node_split = node.split(" = ")
        key = node_split[0]
        value = node_split[-1].replace("(", "").replace(")", "").split(", ")

        node_map[key] = (value[0], value[1])

    node = "AAA"
    steps = 0

    while node != "ZZZ":
        for char in camel_path:
            steps += 1
            next_node = node_map[node][path_map[char]]
            node = next_node

    print(f"{steps}: {node}")


def part_2(input):
    camel_path = input[0]
    node_list = input[1].split("\n")

    path_map = {"L": 0, "R": 1}

    node_map = {}

    nodes = []

    for node in node_list:
        key = node[0:3]
        left_value = node[7:10]
        right_value = node[12:15]

        if key[2] == "A":
            nodes.append(key)

        node_map[key] = (left_value, right_value)

    steps = 0

    # brute force not effective here, need to use LCM bc these loops happen to be cyclical
    y = []
    z = 0
    e = len(nodes)
    print(nodes)
    while z < e:
        for char in camel_path:
            steps += 1
            for i in range(len(nodes)):
                nodes[i] = node_map[nodes[i]][path_map[char]]
            for x in nodes:
                if x[2] == "Z":
                    z += 1
                    print(nodes)
                    nodes.remove(x)
                    y.append(steps)
    print(y)
    print(reduce(lcm, y))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_data = file.read().split("\n\n")

    part_1(input_data)

    part_2(input_data)
