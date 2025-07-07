import math


def solve(n):

    if n == 1:
        return 0

    candidates = [1]

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:

            if i <= 10000000:
                candidates.append(i)

            if n // i <= 10000000:
                candidates.append(n // i)

    return max(candidates)


def solution(begin, end):

    return [solve(i) for i in range(begin, end + 1)]
