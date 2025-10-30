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


with open("Data/_10_1.txt") as f:
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

        step += 1
        if (current_y, current_x) == S:
            break

    print(f"Farthest point: {step / 2}")
