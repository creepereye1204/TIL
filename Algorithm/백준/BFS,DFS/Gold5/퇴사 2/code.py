# dp[종료일] = max(이전까지의 수익+현재 수익, dp[종료일])
n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i - 1], dp[i])
    if t + i - 1 <= n:
        dp[i + t - 1] = max(dp[i + t - 1], dp[i - 1] + p)
print(dp[-1])
