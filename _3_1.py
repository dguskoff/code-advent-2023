import re

num_matches_list = []
symbol_matches_list = []
part_number = 0


def is_part_number(symbol_records, i, num_start_pos, num_end_pos):
    for symbol_position in symbol_records[i]:
        if symbol_position >= num_start_pos and symbol_position <= num_end_pos:
            return True
    if i > 0:
        for symbol_position in symbol_records[i - 1]:
            if symbol_position >= num_start_pos and symbol_position <= num_end_pos:
                return True
    if i < (len(symbol_records) - 1):
        for symbol_position in symbol_records[i + 1]:
            if symbol_position >= num_start_pos and symbol_position <= num_end_pos:
                return True
    return False


def extract_numbers_and_symbols(num_matches_list, symbol_matches_list, f):
    for line in f.readlines():
        num_matches = [
            (m.start() - 1, m.end(), int(m[0]))
            for m in re.finditer(r"\d+", line)
            if m is not None
        ]
        symbol_matches = [
            m.start()
            for m in re.finditer(re.compile(r"[^\\\n0-9a-zA-Z.]+"), line)
            if m is not None
        ]
        num_matches_list.append(num_matches)
        symbol_matches_list.append(symbol_matches)


with open("Data/_3_1.txt") as f:
    extract_numbers_and_symbols(num_matches_list, symbol_matches_list, f)

    i = 0
    while i < len(num_matches_list):
        for num_start_pos, num_end_pos, number in num_matches_list[i]:
            if is_part_number(symbol_matches_list, i, num_start_pos, num_end_pos):
                part_number += number
        i += 1
print(f"Part Number: {part_number}")
