from collections import *
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[987654321 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                dist[i][j] = 0
        if q:
            break

    while q:
        x, y, c = q.popleft()

        if board[x][y] == 'G':
            return c

        for i in range(4):
            n_x = x
            n_y = y

            while 0 <= n_x+dx[i] < N and 0 <= n_y+dy[i] < M and board[n_x+dx[i]][n_y+dy[i]] != 'D':
                n_x += dx[i]
                n_y += dy[i]

            if dist[n_x][n_y] > c+1:
                dist[n_x][n_y] = c+1
                q.append((n_x, n_y, c+1))

    return -1
