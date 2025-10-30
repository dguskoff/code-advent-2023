import re

max_red = 12
max_green = 13
max_blue = 14

sum_ids = 0


def get_max_counts_for_color(cubes, color):
    counts = sorted([c[0] for c in cubes if c[1] == color], reverse=True)
    return counts[0] if len(counts) > 0 else None


def get_max_counts_in_set(game_sets):
    all_cubes = []
    for game_set in game_sets:
        cubes = game_set.split(",")
        for cube in cubes:
            count = int(re.findall(r"\d+", cube)[0])
            color = re.findall(r"[^-0-9\/]+", cube.strip())[0].strip()
            all_cubes.append((count, color))
    return (
        get_max_counts_for_color(all_cubes, "red"),
        get_max_counts_for_color(all_cubes, "green"),
        get_max_counts_for_color(all_cubes, "blue"),
    )


sum_of_power = 0
with open("Data/game_sets.txt") as f:
    for line in f.readlines():
        is_not_possible_flag = False
        game = line.split(":")
        game_id = int(re.findall(r"\d+", game[0])[0])
        game_sets = game[1].split(";")
        (r, g, b) = get_max_counts_in_set(game_sets)
        sum_of_power += r * g * b
print(f"Red: {sum_of_power}")
