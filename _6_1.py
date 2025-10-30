import re
import numpy as np


def read_input_data(f):
    times = []
    distances = []
    time_line = f.readline().split(":")
    times.append([int(n) for n in re.split("\s+", time_line[1].strip())])

    distance_line = f.readline().split(":")
    distances.append([int(n) for n in re.split("\s+", distance_line[1].strip())])

    return list(zip(times[0], distances[0]))


with open("Data/_6_1.txt") as f:
    race = read_input_data(f)

    all_wins = []
    for time, distance in race:
        button_pressed = 0
        wins = 0
        while button_pressed < time:
            if (time - button_pressed) * button_pressed > distance:
                wins += 1
            button_pressed += 1
        all_wins.append(wins)

    num_of_ways = np.prod(all_wins)

    print(f"Numbers of ways to to beat the record: {num_of_ways}")
