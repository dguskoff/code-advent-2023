import re

total_points = 0


def get_points(count):
    points = 1
    i = 1
    for i in range(count + 1):
        if i > 1:
            points = points * 2
    return 0 if count == 0 else points


with open("Data/_4_1.txt") as f:
    for line in f.readlines():
        card = line.split(":")
        card_id = int(re.findall(r"\d+", card[0])[0])
        card_both_sets = card[1].split("|")
        winning_numbers = set(
            [int(n) for n in re.split("\s+", card_both_sets[0].strip())]
        )
        guessed_numbers = set(
            [int(n) for n in re.split("\s+", card_both_sets[1].strip())]
        )
        numbers_won = guessed_numbers.intersection(winning_numbers)

        total_points += get_points(len(numbers_won))

        print(f"Won: {len(numbers_won)}; Points: {get_points(len(numbers_won))}")

print(f"Total points: {total_points}")
