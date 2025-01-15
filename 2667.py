from collections import deque

result = []
N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def bfs(x, y):
    global visited, graph
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(x, y)])
    visited[y][x] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < N and 0 <= y_ < N and not visited[y_][x_] and graph[y_][x_] != "0":
                visited[y_][x_] = True
                cnt += 1
                q += [(x_, y_)]
    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] != "0" and not visited[i][j]:
            result += [bfs(j, i)]


print(len(result))
for r in sorted(result):
    print(r)
