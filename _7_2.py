import re
from collections import Counter
from enum import Enum
from collections import Counter

card_deck = "J23456789TQKA"


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


def getType(hand: list[str]) -> hand_type:
    count = Counter(hand)
    j_count = count.pop("J", 0)
    maxCard = max(count, key=count.get, default="")
    for _ in range(j_count):
        count[maxCard] = min(count[maxCard] + 1, 5)
    count = sorted(list(count.values()) + [j_count * (not maxCard)], reverse=True)
    match count:
        case [5, *_]:
            return hand_type.FIVE
        case [4, *_]:
            return hand_type.FOUR
        case [3, 2, *_]:
            return hand_type.FULLHOUSE
        case [3, _, *_]:
            return hand_type.THREE
        case [2, 2, *_]:
            return hand_type.TWOPAIR
        case [2, *_]:
            return hand_type.ONEPAIR
        case _:
            return hand_type.HIGHCARD


def assign_types_to_hands(
    hand_type: hand_type, hands: list[str]
) -> list[(str, int, int)]:
    hands_with_types = []

    for hand in hands:
        hands_with_types.append((hand[0], hand[1], getType(hand[0]).value))
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
    rank = 1
    all_hands_sorted = []
    all_tests = []
    for cards, bid, c in list_of_type:
        all_tests.append((bid * rank, cards, bid, rank))
        all_hands_sorted.append((bid * rank))
        rank += 1
    return all_hands_sorted


with open("Data/_7_1.txt") as f:
    hands = get_hands(f)

    hands_with_types = assign_types_to_hands(hand_type, hands)

    sorted_by_type = [
        *sort_hand_deck_by_type(card_deck, hand_type.HIGHCARD, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.ONEPAIR, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.TWOPAIR, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.THREE, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.FULLHOUSE, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.FOUR, hands_with_types),
        *sort_hand_deck_by_type(card_deck, hand_type.FIVE, hands_with_types),
    ]

    all_hands_sorted = get_bid_mult_rank(sorted_by_type)

    print(f"Total winnings: {sum(all_hands_sorted)}")
