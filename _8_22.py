import re
import math


def create_instructions(f) -> (str, dict):
    turn_instructions = f.readline().rstrip()
    f.readline()
    node_map = {}
    for l in f.readlines():
        node = l.split("=")
        n = [re.sub("[,()]", "", n) for n in re.split("\s+", node[1].strip())]
        node_map.update({node[0].strip(): (n[0], n[1])})
    return (turn_instructions, node_map)


def find_next_node(source_node: str, step: str, node_map: dict) -> str:
    left_node, right_node = node_map[source_node]
    return left_node if step == "L" else right_node


with open("Data/_8_1.txt") as f:
    turn_instructions, node_map = create_instructions(f)

    As = [a for a in node_map if a.endswith("A")]
    Zs = []

    for a in As:
        next_node = a
        total_steps = 0
        step = 0
        while not next_node.endswith("Z"):
            next_node = find_next_node(next_node, turn_instructions[step], node_map)
            step = 0 if step == len(turn_instructions) - 1 else step + 1
            total_steps += 1

        Zs.append(total_steps)
        print(f"Found {next_node} for {a} . Total steps : {total_steps}")

    answer = math.lcm(*Zs)

    print(f"Total steps from ..A to ..Z for ALL: {answer}")
