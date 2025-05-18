from collections import deque
answer = 0


def bfs(x, y, h, w, tx, ty, maps):
    global answer
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([[x, y]])
    visited = [[-1]*w for _ in range(h)]
    visited[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x+dx[i]
            y_ = y+dy[i]
            if -1 < x_ < w and -1 < y_ < h and visited[y_][x_] == -1 and maps[y_][x_] != 'X':
                visited[y_][x_] = visited[y][x]+1

                q.append([x_, y_])
                if y_ == ty and x_ == tx:
                    answer += visited[y_][x_]
                    return True
    return False


def solution(maps):
    global answer
    h = len(maps)
    w = len(maps[0])
    x1 = y1 = x2 = y2 = x3 = y3 = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'L':
                x2 = j
                y2 = i
            if maps[i][j] == 'E':
                x3 = j
                y3 = i
            if maps[i][j] == 'S':
                x1 = j
                y1 = i

    if not bfs(x1, y1, h, w, x2, y2, maps):
        return -1
    if not bfs(x2, y2, h, w, x3, y3, maps):
        return -1

    return answer
