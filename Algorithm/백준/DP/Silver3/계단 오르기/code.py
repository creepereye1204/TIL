n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [[0] * 2 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0][0] = stairs[0]
    elif i == 1:
        dp[1][0] = sum(stairs[:2])
        dp[1][1] = stairs[1]
    else:
        dp[i][0] = dp[i - 1][1] + stairs[i]
        dp[i][1] = max(dp[i - 2]) + stairs[i]

print(max(dp[n - 1]))
