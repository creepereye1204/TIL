from itertools import combinations
from collections import deque
import sys

INF = sys.maxsize


def bfs(virus):
    global n, graph
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque(virus)
    visited = [[-1] * n for _ in range(n)]
    for x, y in virus:
        visited[y][x] = 0
    mx = -1
    while q:
        x, y = q.popleft()
        mx = max(mx, visited[y][x])
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and visited[y_][x_] == -1 and graph[y_][x_] != 1:  # <-실수한 부분 1
                visited[y_][x_] = visited[y][x] + 1
                q += [(x_, y_)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] != 1:  # <-실수한 부분 2
                return -1

    return mx


n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
viruses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses += [(j, i)]
rst = INF
for virus in list(combinations(viruses, m)):
    v = bfs(virus)
    if v != -1:
        rst = min(rst, v)
print(rst if rst != INF else -1)
