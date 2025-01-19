import sys

input = sys.stdin.readline


def solution(x):
    dp = [1] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(3, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[x]


T = int(input())
for _ in range(T):
    print(solution(int(input())))
