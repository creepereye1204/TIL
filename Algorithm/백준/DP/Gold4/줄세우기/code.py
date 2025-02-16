n = int(input())
dp = [(0, 0) for _ in range(n + 1)]

for i in range(1, n + 1):
    x = int(input())
    mx = -1
    for j in range(i):
        if dp[j][0] < x:
            mx = max(mx, dp[j][1] + 1)
    dp[i] = (x, mx)
print(n - max(list(zip(*dp))[1]))
