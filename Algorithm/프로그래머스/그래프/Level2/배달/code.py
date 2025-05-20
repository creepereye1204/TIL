import heapq


def dijkstra(graph, dist):
    queue = []
    heapq.heappush(queue, [0, 0])
    while queue:
        cost, node = heapq.heappop(queue)

        for v, n in graph[node]:
            if cost+v < dist[n]:
                dist[n] = cost+v
                heapq.heappush(queue, [dist[n], n])


def solution(N, road, K):
    graph = [[] for _ in range(N)]
    for start, end, cost in road:
        graph[start-1].append([cost, end-1])
        graph[end-1].append([cost, start-1])
    dist = [float('inf')]*N
    dist[0] = 0
    dijkstra(graph, dist)
    return len([x for x in dist if x <= K])
