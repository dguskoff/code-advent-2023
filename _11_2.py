import re
from itertools import combinations

TIMES_EXPENDED = 1000000


def get_range(start, end):
    return range(start, end) if start <= end else range(end, start)


def calc_x_or_y(TIMES_EXPENDED, get_range, empty_lines, p_start, p_end):
    num_of_empty = len([v for v in empty_lines if v in get_range(p_start, p_end)])
    return abs(p_end - p_start) - num_of_empty + (num_of_empty * TIMES_EXPENDED)


space_map = open("Data/_11.txt").read().splitlines()

empty_hor = [i for i, l in enumerate(space_map) if re.search(r"#", l) is None]

empty_vert = [
    i
    for i in range(len(space_map[0]))
    if len([l[i] for l in space_map if l[i] != "."]) == 0
]

gxs = [
    (ind, g.start())
    for ind, line in enumerate(space_map)
    for g in re.finditer(r"#", line)
]

all_pairs = list(combinations(gxs, 2))

distances = [
    calc_x_or_y(TIMES_EXPENDED, get_range, empty_vert, p[1][1], p[0][1])
    + calc_x_or_y(TIMES_EXPENDED, get_range, empty_hor, p[1][0], p[0][0])
    for p in all_pairs
]

print(f"Total: {sum(distances)}")
