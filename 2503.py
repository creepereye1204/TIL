import sys
from itertools import permutations

input = sys.stdin.readline


def solve(combinations, arrs):
    for arr in arrs:

        for combination in combinations:
            strikes = 0
            balls = 0
            for i in range(3):
                if combination[i] == int(str(arr[0])[i]):
                    strikes += 1
                elif int(str(arr[0])[i]) in combination:
                    balls += 1
            if arr[1] == strikes and arr[2] == balls:
                pass
            else:
                combinations = combinations - {combination}
    print(len(combinations))


def main():
    combinations = set(
        permutations(
            [
                i
                for i in range(
                    1,
                    10,
                )
            ],
            3,
        )
    )
    n = int(input())
    arrs = tuple(tuple(map(int, input().split(" "))) for _ in range(n))
    solve(combinations, arrs)


if __name__ == "__main__":
    main()
