t = int(input())
for _ in range(t):

    n = int(input())
    p = list(map(int, input().split(' ')))
    m = int(input())
    dp = [0]*(m+1)
    dp[0] = 1
    for i in range(n):
        for j in range(p[i], m+1):

            dp[j] += dp[j-p[i]]
    print(dp[-1])
