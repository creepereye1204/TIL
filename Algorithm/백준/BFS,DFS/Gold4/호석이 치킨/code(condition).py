from collections import deque
from itertools import combinations

n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a] += [b]
    graph[b] += [a]


def bfs(nodes):
    visited = set(nodes)
    q = deque(nodes)
    dist = [0] * (n + 1)

    while q:
        node = q.popleft()
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                q += [v]
                dist[v] = dist[node] + 1

    return [min(nodes), max(nodes), 2 * sum(dist)]


rst = []
for nodes in list(combinations(list(range(1, n + 1)), 2)):
    rst += [bfs(nodes)]
rst.sort(key=lambda x: (x[2], x[0], x[1]))
print(*rst[0])
