from collections import deque


def solution():
    answer = 0
    n, v = map(int, input().split(" "))
    graph = [[] for _ in range(n + 1)]
    visited = []
    for _ in range(v):
        a, b = map(int, input().split(" "))
        graph[a] += [b]
        graph[b] += [a]

    for i in range(1, n + 1):
        if i not in visited:
            visited += [i]
            answer += 1
            bfs(graph, visited, i)
    print(answer)


def bfs(graph, visited, i):
    q = deque([i])
    while q:
        v = q.popleft()
        for node in graph[v]:
            if node not in visited:
                visited += [node]
                q.append(node)


solution()
