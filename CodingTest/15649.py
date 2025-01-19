from itertools import permutations


def solution(x, y):
    for value in permutations(list(range(1, x + 1)), y):
        for v in value:
            print(v, end=" ")
        print()


x, y = map(int, input().split(" "))
solution(x, y)
