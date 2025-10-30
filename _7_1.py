import re
from collections import Counter
from enum import Enum

card_deck = "23456789TJQKA"


class hand_type(Enum):
    FIVE = 7
    FOUR = 6
    FULLHOUSE = 5
    THREE = 4
    TWOPAIR = 3
    ONEPAIR = 2
    HIGHCARD = 1
    UNKNOWN = 0


def get_hands(f):
    hands_init = []
    for line in f.readlines():
        hands_init.append([n for n in re.split("\s+", line.strip())])
    return [(card, int(bid)) for card, bid in hands_init]


def assign_types_to_hands(hand_type, hands):
    hands_with_types = []
    type = hand_type.UNKNOWN
    for hand in hands:
        dupe_counts = dict(Counter(hand[0]))
        dupes_list = [count for letter, count in dupe_counts.items() if count > 1]
        if len(dupes_list) == 0:
            type = hand_type.HIGHCARD
        elif len(dupes_list) == 1:
            if dupes_list[0] == 2:
                type = hand_type.ONEPAIR
            elif dupes_list[0] == 5:
                type = hand_type.FIVE
            elif dupes_list[0] == 4:
                type = hand_type.FOUR
            elif dupes_list[0] == 3:
                type = hand_type.THREE
        else:
            if dupes_list[0] == 2 and dupes_list[1] == 2:
                type = hand_type.TWOPAIR
            elif (
                dupes_list[0] == 2
                and dupes_list[1] == 3
                or dupes_list[0] == 3
                and dupes_list[1] == 2
            ):
                type = hand_type.FULLHOUSE
        hands_with_types.append((hand[0], hand[1], type.value))
        hands_with_types.sort(key=lambda a: a[2], reverse=True)
    return hands_with_types


def sort_hand_deck_by_type(card_deck, hand_type, hands_with_types):
    this_type = [
        (card, bid, type)
        for card, bid, type in hands_with_types
        if type == hand_type.value
    ]
    order = dict(zip(card_deck, range(len(card_deck))))
    return sorted(this_type, key=lambda word: [order[c] for c in word[0]])


def get_bid_mult_rank(list_of_type):
    global rank
    all_hands_sorted = []

    for cards, bid, c in list_of_type:
        all_hands_sorted.append(bid * rank)
        rank += 1
    return all_hands_sorted


with open("Data/_7_tt.txt") as f:
    hands = get_hands(f)

    hands_with_types = assign_types_to_hands(hand_type, hands)

    five_of_kind = sort_hand_deck_by_type(card_deck, hand_type.FIVE, hands_with_types)
    four_of_kind = sort_hand_deck_by_type(card_deck, hand_type.FOUR, hands_with_types)
    three_of_kind = sort_hand_deck_by_type(card_deck, hand_type.THREE, hands_with_types)
    full_house = sort_hand_deck_by_type(
        card_deck, hand_type.FULLHOUSE, hands_with_types
    )
    one_pair = sort_hand_deck_by_type(card_deck, hand_type.ONEPAIR, hands_with_types)
    two_pair = sort_hand_deck_by_type(card_deck, hand_type.TWOPAIR, hands_with_types)
    high_pair = sort_hand_deck_by_type(card_deck, hand_type.HIGHCARD, hands_with_types)

    all_hands_sorted = []
    rank = 1
    all_hands_sorted.extend(get_bid_mult_rank(high_pair))
    all_hands_sorted.extend(get_bid_mult_rank(one_pair))
    all_hands_sorted.extend(get_bid_mult_rank(two_pair))
    all_hands_sorted.extend(get_bid_mult_rank(three_of_kind))
    all_hands_sorted.extend(get_bid_mult_rank(full_house))
    all_hands_sorted.extend(get_bid_mult_rank(four_of_kind))
    all_hands_sorted.extend(get_bid_mult_rank(five_of_kind))

    su = sum(all_hands_sorted)
    print(f"Total winnings: {sum(all_hands_sorted)}")
