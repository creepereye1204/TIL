from collections import deque


def bfs():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n, m = map(int, input().split(" "))
    table = [list(map(int, input().split(" "))) for _ in range(n)]
    count = [[-1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 2:
                x, y = j, i
                break
    q = deque([(x, y)])
    visited[y][x] = True
    count[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < m and 0 <= y_ < n and not visited[y_][x_] and table[y_][x_] != 0:
                visited[y_][x_] = True
                count[y_][x_] = count[y][x] + 1
                q += [(x_, y_)]

    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                print(0, end=" ")
            else:
                print(count[i][j], end=" ")
        print()


bfs()
