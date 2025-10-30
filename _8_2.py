import re


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

    total_steps = 0
    step = 0

    dest = []
    ends_with_z = [" "]
    while len(dest) != len(ends_with_z):
        total_steps += 1
        dest.clear()
        ends_with_z.clear()
        for a in As:
            dest.append(find_next_node(a, turn_instructions[step], node_map))
        step = 0 if step == len(turn_instructions) - 1 else step + 1
        ends_with_z = [x for x in dest if x.endswith("Z")]
        As = dest.copy()
        if total_steps % 1000000 == 0:
            print(f"Total steps {total_steps}")

    print(f"Total steps from AAA to ZZZ for all paths: {total_steps}")
