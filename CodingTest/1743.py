from collections import deque


def bfs(x, y):
    global visited, arr, n, m
    visited[y][x] = True
    cnt = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < m and 0 <= y_ < n and arr[y_][x_] and not visited[y_][x_]:
                cnt += 1
                visited[y_][x_] = True
                q += [(x_, y_)]
    return cnt


n, m, k = map(int, input().split(" "))
arr = [[False] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
rst = -1
for _ in range(k):
    a, b = map(int, input().split(" "))
    arr[a - 1][b - 1] = True

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            rst = max(bfs(j, i), rst)


print(rst)
