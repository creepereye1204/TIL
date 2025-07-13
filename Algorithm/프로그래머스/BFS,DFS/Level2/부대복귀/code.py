from collections import deque

def solution(n, roads, sources, destination):
    l = len(sources)
    answer = [-1] * l
    dist = [-1] * (n + 1)
    q = deque([destination])
    dist[destination] = 0
    graph = [[] for _ in range(n + 1)]


    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    while q:
        node = q.popleft()
        d=dist[node] + 1
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = d
                q.append(next_node)
    return [dist[source] for source in sources]