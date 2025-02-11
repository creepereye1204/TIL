import sys

a, b = map(int, input().split())
INF = sys.maxsize
dp = [INF] * (b + 1)
coins = set()
for _ in range(a):
    x = int(input())
    coins.add(x)
dp[0] = 0


for coin in coins:
    for i in range(coin, b + 1):

        dp[i] = min(dp[i - coin] + 1, dp[i])

print(dp[b] if dp[b] != INF else -1)
