import random

MAIN_CIRCLE = list(("A", "B", "C", "D", "E", "F"))
SUBCIRCLE_LEN = 4
SUBCIRCLES = 3

# harcoded graph
ADJACANCY_LISTS = {
    0: (2, 3, 4, 5),
    1: (2, 4, 5),
    2: (0, 1, 3),
    3: (0, 2),
    4: (0, 1),
    5: (0, 1)
}

PAIRS_LIST = [(1, 4), (2, 3), (0, 3), (0, 5), (0, 2), (1, 2), (1, 5), (0, 4)]


def get_pairs():
    pairs_set = set()
    for item_from in ADJACANCY_LISTS:
        for item_to in ADJACANCY_LISTS[item_from]:
            pairs_set.add(
                tuple((min(item_from, item_to), max(item_from, item_to))))
    return pairs_set


def get_pairs_list(pairs_set):
    return random.sample(list(pairs_set), len(pairs_set))


def game():
    # pairs_set = get_pairs()
    # pairs_list = get_pairs_list(pairs_set)

    pairs_list = PAIRS_LIST


game()
