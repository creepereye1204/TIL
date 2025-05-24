from collections import deque


def bfs(visited, maps, x, y, h, w):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque([[x, y]])
    visited[y][x] = True
    rst = int(maps[y][x])
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if 0 <= x_ < w and 0 <= y_ < h and not visited[y_][x_] and maps[y_][x_].isdigit():
                rst += int(maps[y_][x_])
                visited[y_][x_] = True
                q.append([x_, y_])
    return rst


def solution(maps):
    answer = []
    h = len(maps)
    w = len(maps[0])
    visited = [[False]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if maps[y][x].isdigit() and not visited[y][x]:
                answer.append(bfs(visited, maps, x, y, h, w))

    return sorted(answer) if answer else [-1]
