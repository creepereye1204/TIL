from itertools import combinations
from collections import deque


def bfs(x, y, spots):
    global n, graph, dx, dy
    visited = [[-1] * n for _ in range(n)]
    q = deque([(x, y)])
    visited[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and visited[y_][x_] == -1:
                visited[y_][x_] = visited[y][x] + 1
                if (x_, y_) in spots:

                    return visited[y_][x_]
                q.append((x_, y_))


rst = 1000000000
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

chikens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chikens += [(j, i)]

for spots in list(combinations(chikens, m)):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                cnt += bfs(j, i, spots)

    rst = min(rst, cnt)


print(rst)
