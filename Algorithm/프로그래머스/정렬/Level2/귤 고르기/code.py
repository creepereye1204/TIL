from collections import Counter


def solution(k, tangerine):
    oranges = sorted(Counter(tangerine).values(), reverse=True)
    cnt = 0
    for value in oranges:
        if k > 0:
            k -= value
            cnt += 1
        else:
            break
    return cnt
