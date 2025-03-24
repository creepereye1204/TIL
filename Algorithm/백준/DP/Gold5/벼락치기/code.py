n, t = map(int, input().split(' '))
dp = [[0]*(t+1) for _ in range(n+1)]
p = [[]]
for _ in range(n):
    a, b = map(int, input().split(' '))
    p.append((a, b))


for i in range(1, n+1):
    time = p[i][0]
    score = p[i][1]
    for j in range(1, t+1):
        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time]+score)

print(dp[n][-1])
