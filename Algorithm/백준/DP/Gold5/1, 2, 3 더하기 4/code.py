dp = [1]*10_101

for i in range(2, 10_101):
    dp[i] += dp[i-2]


for i in range(3, 10_101):
    dp[i] += dp[i-3]

for _ in range(int(input())):
    print(dp[int(input())])
