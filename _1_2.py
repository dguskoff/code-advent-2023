import re


def get_all_matches(line, list_of_items):
    matches = []
    for i, item in enumerate(list_of_items, start=1):
        findings = [(m.start(), i) for m in re.finditer(item, line) if m is not None]
        for finding in findings:
            if finding is not None:
                matches.append(finding)
    return matches


lit_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dig_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

calibration = 0

with open("Data/calibrations.txt") as f:
    for line in f.readlines():
        matches = []
        for match in get_all_matches(line, lit_numbers):
            matches.append(match)
        for match in get_all_matches(line, dig_numbers):
            matches.append(match)
        sorted_matches = sorted(matches)
        if len(sorted_matches) > 0:
            calibration += sorted_matches[0][1] * 10 + sorted_matches[-1][1]

print(f"Total calibration: {calibration}")
