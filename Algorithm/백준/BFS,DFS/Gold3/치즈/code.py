from collections import deque

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
flage = True
time = -1


def bfs(j, i, visited):
    q = deque([[j, i]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[i][j] = True
    trash = []
    while q:
        x, y = q.popleft()
        cnt = 0
        for k in range(4):
            x_ = dx[k] + x
            y_ = dy[k] + y
            if 0 <= x_ < m and 0 <= y_ < n and graph[y_][x_] == 0:
                cnt += 1
        if cnt > 1:
            trash += [[x, y]]
        for k in range(4):
            x_ = dx[k] + x
            y_ = dy[k] + y
            if 0 <= x_ < m and 0 <= y_ < n and graph[y_][x_] == 1 and not visited[y_][x_]:
                visited[y_][x_] = True
                q += [[x_, y_]]

    for x, y in trash:
        graph[y][x] = 0


while flage:
    flage = False
    time += 1
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(j, i, visited)
                flage = True
    print()
    for t in graph:

        print(*t)

print(time, end="")
