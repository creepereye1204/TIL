import sys

sys.setrecursionlimit(10**6)
answer = 0


def dfs(idx, cnt, n, target, numbers):
    global answer
    if idx == n - 1:

        if target == cnt:
            answer += 1
        return

    dfs(idx + 1, cnt - numbers[idx + 1], n, target, numbers)
    dfs(idx + 1, cnt + numbers[idx + 1], n, target, numbers)


def solution(numbers, target):
    global answer
    dfs(0, numbers[0], len(numbers), target, numbers)
    dfs(0, -numbers[0], len(numbers), target, numbers)
    return answer
