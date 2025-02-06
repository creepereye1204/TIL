from itertools import combinations
import sys

INF = sys.maxsize
n, m = map(int, input().split(" "))

dp = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    dp[a][b] = dp[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


rst = [INF] * 3
for nodes in list(combinations(list(range(1, n + 1)), 2)):
    mn, mx = min(nodes), max(nodes)
    dist = 2 * sum([min(dp[mn][i], dp[mx][i]) for i in range(1, n + 1)])
    toggle = False
    if rst[2] > dist:
        toggle = True
    elif rst[2] == dist:
        if mn < rst[0]:
            toggle = True
        elif mn == rst[0]:
            if mx > rst[1]:
                toggle = True
    if toggle:
        rst = [mn, mx, dist]
print(*rst)
