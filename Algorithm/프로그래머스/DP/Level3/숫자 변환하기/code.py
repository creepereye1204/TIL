import sys


def solution(x, y, n):
    INF = sys.maxsize
    dp = [INF]*(y+1)
    dp[x] = 0
    for i in range(x+1, y+1):
        if n < i:
            dp[i] = min(dp[i-n]+1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])
    return dp[y] if dp[y] != INF else -1
