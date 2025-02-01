n = int(input())
dp = [[0] * 2 for _ in range(n)]
p = []
for _ in range(n):
    p += [int(input())]

for i in range(n):
    if i == 0:
        dp[i][1] = p[i]
    elif i == 1:
        dp[i][1] = p[i - 1] + p[i]
        dp[i][0] = p[i - 1]
    else:

        dp[i][1] = max(dp[i - 2][1], dp[i - 2][0] + p[i - 1]) + p[i]
        dp[i][0] = max(dp[i - 1])
print(max(dp[n - 1]))
