n = int(input())
dp = [-1] * (n + 1)
p, t = [0], [0]
for i in range(n):
    a, b = map(int, input().split(" "))
    t += [a]
    p += [b]
for i in range(1, n + 1):
    c = i + t[i] - 1
    if c <= n:
        dp[c] = p[i]
# for i in range(n):
#     c = i + t[i]
#     if c < n:
#         dp[c] = max(dp[c], dp[i] + p[i])
print(dp)
