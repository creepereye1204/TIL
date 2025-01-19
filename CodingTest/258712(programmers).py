from collections import defaultdict
from itertools import combinations


def solution(friends, gifts):
    giver_table = defaultdict(lambda: defaultdict(int))
    zisu_table = defaultdict(int)
    answer = defaultdict(int)

    for gift in gifts:
        giver, taker = gift.split(" ")
        giver_table[giver][taker] += 1
        zisu_table[giver] += 1
        zisu_table[taker] -= 1

    for giver, taker in combinations(friends, 2):
        a = giver_table[giver][taker]
        b = giver_table[taker][giver]

        if a < b:
            answer[taker] += 1
        elif a > b:
            answer[giver] += 1
        else:
            if zisu_table[taker] < zisu_table[giver]:
                answer[giver] += 1
            elif zisu_table[taker] > zisu_table[giver]:
                answer[taker] += 1

    return max(answer.values() if answer.values() else [0])
