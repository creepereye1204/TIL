from collections import deque


def bfs(graph):
    q = deque([[1, 0]])
    visited = set([1])
    rst = []
    while q:
        y, cnt = q.popleft()
        for node in graph[y]:

            if not ({node} & visited):

                visited.add(node)

                q += [[node, cnt + 1]]
                rst += [cnt + 1]
    mx = max(rst)
    return rst.count(mx)


def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]

    for a, b in vertex:
        graph[a] += [b]
        graph[b] += [a]

    return bfs(graph, n)
