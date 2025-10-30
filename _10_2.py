import re

pipe_maps = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["w", "s"],
    "F": ["e", "s"],
}


def to_from(to: str) -> str:
    match to:
        case "w":
            return "e"
        case "e":
            return "w"
        case "s":
            return "n"
        case "n":
            return "s"


def find_next_pipe(
    field: list[str], current_y: int, current_x: int, go_to
) -> (str, int, int):
    next_y, next_x = current_y, current_x
    match go_to:
        case "e":
            next_x += 1
        case "w":
            next_x -= 1
        case "s":
            next_y += 1
        case "n":
            next_y -= 1

    return field[next_y][next_x], next_y, next_x


def replace_by_index(string, idx, character):
    return string[:idx] + character + string[idx + 1 :]


x_num = 0


def get_repl_character(char: str, field_row: str, ind: int) -> str:
    global x_num
    if char == "X":
        x_num += 1

    if char == "." and ind == 0 or char == "." and ind == len(field_row) - 2:
        return "."
    elif char == "." and x_num == 0:
        return "."
    elif char == "." and x_num != 0 and x_num % 2 != 0:
        res = re.search("X", field_row[ind:])
        if res is None:
            return "."
        else:
            return "*"
    else:
        return char


with open("Data/_10_t3.txt") as f:
    field = f.readlines()
    S = [(ind, l.find("S")) for ind, l in enumerate(field) if "S" in l][0]
    go_to, first_type = "e", "F"

    current_y, current_x = S
    current_type = first_type
    step = 0
    while True:
        go_to = [m for m in pipe_maps[current_type] if to_from(go_to) not in m][0]
        current_type, current_y, current_x = find_next_pipe(
            field, current_y, current_x, go_to
        )

        field[current_y] = replace_by_index(field[current_y], current_x, "X")

        step += 1
        if (current_y, current_x) == S:
            break

    for ind, f in enumerate(field):
        x_num = 0
        if ind == 9:
            s = ""

        updated_str = "".join(
            [get_repl_character(char, f, ind) for ind, char in enumerate(f)]
        )
        field[ind] = updated_str

    for ind, f in enumerate(field):
        print(ind, f)

    total_I = 0
    for f in field:
        all_I_in_line = re.findall("\*", f)
        total_I += len(all_I_in_line)

    print(f"Total inside: {total_I}")
