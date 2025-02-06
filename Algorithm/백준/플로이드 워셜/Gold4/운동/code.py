import sys

V, E = map(int, input().split(" "))
INF = sys.maxsize
graph = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a - 1][b - 1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

mn = INF
for i in range(V):
    for j in range(V):
        if i == j:
            mn = min(mn, graph[i][j])

print(mn if mn < INF else -1)
