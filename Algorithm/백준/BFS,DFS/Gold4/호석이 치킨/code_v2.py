from collections import deque
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


rst = []
for nodes in list(combinations(list(range(1, n + 1)), 2)):
    mn, mx = min(nodes), max(nodes)
    rst += [[mn, mx, 2 * sum([min(dp[mn][i], dp[mx][i]) for i in range(1, n + 1)])]]
rst.sort(key=lambda x: (x[2], x[0], x[1]))
print(*rst[0])
