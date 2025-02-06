from collections import deque


def bfs(graph, n):
    q = deque([1])
    dist = [-1] * (n + 1)
    dist[1] = 0
    while q:
        node = q.popleft()
        for v in graph[node]:
            if dist[v] == -1:
                dist[v] = dist[node] + 1
                q.append(v)
    return dist.count(max(dist))


def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]

    for a, b in vertex:
        graph[a] += [b]
        graph[b] += [a]

    return bfs(graph, n)
