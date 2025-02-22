from collections import deque

# 모든 높이에서 BFS를 통해 그룹의 개수를 최대치로
rst = 0


def bfs(j, i, visited, depth, board, n):
    q = deque([[j, i]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for index in range(4):
            x_ = x + dx[index]
            y_ = y + dy[index]
            if 0 <= x_ < n and 0 <= y_ < n and board[y_][x_] > depth and not visited[y_][x_]:
                visited[y_][x_] = True
                q += [[x_, y_]]


def run(depth, n, board):
    global rst
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > depth and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                bfs(j, i, visited, depth, board, n)
    rst = max(rst, cnt)


def solution(n):
    global rst

    board = [list(map(int, input().split(" "))) for _ in range(n)]
    for depth in range(0, 101):
        run(depth, n, board)

    print(rst)


solution(int(input()))
