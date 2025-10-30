import re
import math

num_list = []
star_list = []
gear_ratios_sum = 0


def extract_numbers_and_stars(num_matches_list, symbol_matches_list, f):
    for line in f.readlines():
        num_matches = [
            (m.start() - 1, m.end(), int(m[0]))
            for m in re.finditer(r"\d+", line)
            if m is not None
        ]
        star_matches = [
            m.start() for m in re.finditer(re.compile(r"[*]+"), line) if m is not None
        ]
        num_list.append(num_matches)
        star_list.append(star_matches)


def get_adjacent_nums_for_star(num_list, i, star_position):
    return [num for (start, end, num) in num_list[i] if start <= star_position <= end]


with open("Data/_3_1.txt") as f:
    extract_numbers_and_stars(num_list, star_list, f)

    i = 0
    while i < len(star_list):
        for star_position in star_list[i]:
            adjacent_nums_current = get_adjacent_nums_for_star(
                num_list, i, star_position
            )
            if i > 0:
                adjacent_nums_top = get_adjacent_nums_for_star(
                    num_list, i - 1, star_position
                )
            if i < (len(star_list) - 1):
                adjacent_nums_bottom = get_adjacent_nums_for_star(
                    num_list, i + 1, star_position
                )

            all_adjacent_nums = (
                adjacent_nums_current + adjacent_nums_top + adjacent_nums_bottom
            )

            if len(all_adjacent_nums) > 1:
                gear_ratios_sum += math.prod(all_adjacent_nums)

        i += 1
print(f"Sum of Gear ratios: {gear_ratios_sum}")
