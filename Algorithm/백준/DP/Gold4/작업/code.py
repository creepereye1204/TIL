n = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    work, _, *pre = map(int, input().split(" "))
    dp[i] = work
    for j in pre:
        dp[i] = max(dp[i], dp[j] + work)
print(max(dp))
