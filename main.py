import random

NAMES = list(("A", "B", "C", "D", "E", "F"))
# harcoded graph
ADJACANCY_LISTS = {
    0: {2, 3, 4, 5},
    1: {2, 4, 5},
    2: {0, 1, 3},
    3: {0, 2},
    4: {0, 1},
    5: {0, 1}
}
PAIRS_LIST = [(1, 4), (2, 3), (0, 3), (0, 5), (0, 2), (1, 2), (1, 5), (0, 4)]
RESULT_HEADER = "\n============RESULTS============"

assert (len(NAMES) == len(ADJACANCY_LISTS.keys()))


def get_pairs():
    pairs_set = set()
    for item_from in ADJACANCY_LISTS:
        for item_to in ADJACANCY_LISTS[item_from]:
            pairs_set.add(
                tuple((min(item_from, item_to), max(item_from, item_to))))
    return pairs_set


def get_pairs_list(pairs_set):
    return random.sample(list(pairs_set), len(pairs_set))


def ask_next_rate(pair):
    print("По какому курсу будем менять {} на {}: ".format(NAMES[pair[0]],
                                                           NAMES[pair[1]]),
          end='')
    while True:
        try:
            rate_0, rate_1 = [int(i) for i in input().split(' ')]
            assert ((rate_0 > 0) and (rate_1 > 0))
            break
        except (AssertionError, ValueError):
            print("Что-то пошло не так, пожалуйста, снова введите два "
                  "целых числа через пробел: ", end='')

    return rate_0, rate_1


def get_rates(dest, curr, prev, exchange_rates, curr_rate, rate_list):
    for item_to in ADJACANCY_LISTS[curr]:
        if item_to == dest:
            rate_list.append(
                curr_rate * exchange_rates[min(curr, dest)][max(curr, dest)])
        elif item_to == prev:
            continue
        else:
            get_rates(dest,
                      item_to,
                      curr,
                      exchange_rates,
                      curr_rate * exchange_rates[min(curr, item_to)][
                          max(curr, item_to)],
                      rate_list)


def print_result(rate_list):
    print(RESULT_HEADER)
    print("Поздравляем! Один из придуманных вами путей обмена "
          "позволяет обменять 1 {} на {} {}".format(NAMES[0],
                                                    max(rate_list),
                                                    NAMES[0]))


def game():
    # pairs_set = get_pairs()
    # pairs_list = get_pairs_list(pairs_set)

    pairs_list = PAIRS_LIST
    exchange_rates = dict()

    for pair in pairs_list:
        rate_0, rate_1 = ask_next_rate(pair)
        if pair[0] not in exchange_rates:
            exchange_rates[pair[0]] = dict()
        exchange_rates[pair[0]][pair[1]] = rate_1 / rate_0

    rate_list = list()
    get_rates(0, 0, 0, exchange_rates, 1, rate_list)
    print_result(rate_list)

game()
