from itertools import permutations, combinations


def mix(numbers, n):
    combos = []
    for combo in combinations(numbers, n // 2):
        remaining = [num for num in numbers if num not in combo]
        combos.append((combo, tuple(remaining)))
    return combos


def solve(arr1, arr):

    cnt = 0
    for a in arr1:
        for b in arr1:
            cnt += arr[a][b]

    return cnt


def solution():
    answer = float("inf")
    n = int(input())
    numbers = list(range(0, n))
    arr = [list(map(int, input().split(" "))) for _ in range(n)]
    for arr1, arr2 in mix(numbers, n):
        a = solve(arr1, arr)
        b = solve(arr2, arr)

        answer = min(answer, abs(a - b))
    return answer


print(solution())
