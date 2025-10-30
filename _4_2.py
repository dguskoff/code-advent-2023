import re
import time

card_set_init = []
card_set = []
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

        card_set_init.append((card_id, len(numbers_won)))
i = 0
card_set.extend(card_set_init)

t1_start = time.perf_counter()
for card_id, numbers_won in card_set:
    i += 1
    if i == 1 or i % 1000 == 0:
        print(card_id, numbers_won, i, len(card_set), time.perf_counter() - t1_start)

    if numbers_won > 0:
        new_copies = [
            (id, won)
            for (id, won) in card_set_init
            if card_id + numbers_won + 1 > id > card_id
        ]
        card_set.extend(new_copies)


print(f"Total: {len(card_set)}")
