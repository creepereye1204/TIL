from collections import deque


def bfs(i):
    global n, graph
    dist = [-1] * n
    dist[i] = 0
    q = deque([i])
    while q:
        v = q.popleft()
        for node in graph[v]:
            if dist[node] == -1:
                dist[node] = dist[v] + 1
                q += [node]
    return sum(dist)


n, m = map(int, input().split(" "))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a - 1] += [b - 1]
    graph[b - 1] += [a - 1]
mx = 99999999999
rst = -1
for i in range(n):
    temp = bfs(i)
    if mx > temp:
        mx = temp
        rst = i
print(rst + 1)
