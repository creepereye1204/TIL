from collections import deque

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def out(j, i):
    visited = [[False] * m for _ in range(n)]
    q = deque([[j, i]])

    visited[i][j] = True
    graph[i][j] = -1
    while q:
        x, y = q.popleft()

        for k in range(4):
            x_ = dx[k] + x
            y_ = dy[k] + y
            if 0 <= x_ < m and 0 <= y_ < n and not visited[y_][x_] and graph[y_][x_] != 1:
                visited[y_][x_] = True

                q.append((x_, y_))
                graph[y_][x_] = -1


def bfs(j, i):
    out(j, i)
    visited = [[False] * m for _ in range(n)]
    q = deque([[j, i]])

    visited[i][j] = True
    trash = []
    while q:
        x, y = q.popleft()

        for k in range(4):
            x_ = dx[k] + x
            y_ = dy[k] + y
            if 0 <= x_ < m and 0 <= y_ < n and not visited[y_][x_]:
                visited[y_][x_] = True
                if graph[y_][x_] == -1:
                    q.append((x_, y_))
                elif graph[y_][x_] == 1:
                    cnt = 0
                    for h in range(4):
                        x__ = dx[h] + x_
                        y__ = dy[h] + y_
                        if 0 <= x__ < m and 0 <= y__ < n and graph[y__][x__] == -1:
                            cnt += 1
                    if cnt > 1:
                        trash.append((x_, y_))

    for x, y in trash:
        graph[y][x] = -1
    if trash:
        return True
    return False


while bfs(0, 0):
    time += 1

print(time, end="")
