import re
import numpy as np


def read_input_data(f):
    time_line = f.readline().split(":")
    time = "".join(time_line[1].split())

    distance_line = f.readline().split(":")
    distance = "".join(distance_line[1].split())

    return (int(time), int(distance))


with open("Data/_6_t.txt") as f:
    time, distance = read_input_data(f)

    i = 0

    button_pressed = 0
    wins = 0
    while button_pressed < time:
        if (time - button_pressed) * button_pressed > distance:
            wins += 1
        button_pressed += 1

        if i == 0 or i % 1000000 == 0:
            print(f"Ran {i} times")
        i += 1

    print(f"Numbers of ways to to beat the record: {wins}")
