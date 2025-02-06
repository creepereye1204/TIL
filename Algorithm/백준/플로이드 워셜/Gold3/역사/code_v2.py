from collections import deque

N, K = map(int, input().split())
graph = [[0] * (N) for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split(" "))
    graph[a - 1][b - 1] = -1
    graph[b - 1][a - 1] = 1
S = int(input())
questions = [list(map(int, input().split())) for _ in range(S)]
for n in range(N):
    q = deque([n])
    visited = [False] * N

    while q:
        node = q.popleft()
        neighbors = [prior for prior in range(N) if graph[node][prior] == -1]
        for neighbor in neighbors:
            if not visited[neighbor]:
                visited[neighbor] = True
                graph[n][neighbor] = -1
                q += [neighbor]
                graph[neighbor][n] = 1

for question in questions:
    a, b = question[0], question[1]
    print(graph[a - 1][b - 1])
