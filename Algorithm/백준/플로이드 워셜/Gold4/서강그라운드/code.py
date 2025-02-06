import sys

INF = sys.maxsize
n, m, r = map(int, input().split(" "))

items = list(map(int, input().split(" ")))
graph = [[INF] * n for _ in range(n)]
for _ in range(r):
    a, b, c = map(int, input().split(" "))
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
mx = -1
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] <= m:
            cnt += items[j]
    mx = max(mx, cnt)
print(mx)
