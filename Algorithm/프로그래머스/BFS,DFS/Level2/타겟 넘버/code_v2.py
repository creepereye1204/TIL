import sys

sys.setrecursionlimit(10**6)
answer = 0


def dfs(idx, cnt, target, numbers):
    global answer
    if idx == len(numbers) - 1:

        if target == cnt:
            answer += 1
        return

    dfs(idx + 1, cnt - numbers[idx + 1], target, numbers)
    dfs(idx + 1, cnt + numbers[idx + 1], target, numbers)


def solution(numbers, target):
    global answer
    dfs(-1, 0, target, numbers)
    return answer
