import re

max_red = 12
max_green = 13
max_blue = 14

sum_ids = 0


def is_possible(color, count):
    match color:
        case "red":
            return count < max_red + 1
        case "green":
            return count < max_green + 1
        case "blue":
            return count < max_blue + 1
        case _:
            return False


def check_game_sets(is_possible, game_sets):
    for game_set in game_sets:
        cubes = game_set.split(",")
        for cube in cubes:
            count = int(re.findall(r"\d+", cube)[0])
            color = re.findall(r"[^-0-9\/]+", cube.strip())[0].strip()
            if not is_possible(color, count):
                return False
    return True


with open("Data/game_sets.txt") as f:
    for line in f.readlines():
        game = line.split(":")
        game_id = int(re.findall(r"\d+", game[0])[0])
        game_sets = game[1].split(";")
        if check_game_sets(is_possible, game_sets):
            sum_ids += game_id

print(f"Sum of Game Ids: {sum_ids}")
