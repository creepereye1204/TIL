n = int(input())
dp = list(range(n+1))
for i in range(6, n+1):
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
print(dp[-1])
