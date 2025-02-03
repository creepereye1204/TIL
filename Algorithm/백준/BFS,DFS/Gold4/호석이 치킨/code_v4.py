from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline
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


answer_a = answer_b = 0
answer_total = INF
for a, b in combinations(range(n), 2):
    total = 0
    for idx in range(1, n + 1):
        if idx in (a, b):
            continue
        total += min(dp[a][idx], dp[b][idx]) * 2
    if total < answer_total:
        answer_total = total
        answer_a, answer_b = a, b
print(answer_a, answer_b, answer_total)
