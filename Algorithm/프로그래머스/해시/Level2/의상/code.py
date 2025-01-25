from collections import Counter
import math


def solution(clothes):
    clo = Counter([k for i, k in clothes])
    return math.prod([v + 1 for v in clo.values()]) - 1
