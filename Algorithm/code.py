import sys

sys.setrecursionlimit(10**8)
rst = 0
n = int(input())
board = [list(map(int, input().split(" "))) for _ in range(n)]
dx = [1, 1, 0]
dy = [0, 1, 1]


def dfs(x, y, state):
    global board, dx, dy, n, rst

    if x == n - 1 and y == n - 1:
        rst += 1

        return
    if state == 0:
        for i in range(2):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and board[y_][x_] == 0:
                if i == 1:
                    if board[y_ - 1][x_] == 0 and board[y_][x_ - 1] == 0:
                        dfs(x_, y_, i)
                else:
                    dfs(x_, y_, i)
    elif state == 1:
        for i in range(3):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and board[y_][x_] == 0:
                if i == 1:
                    if board[y_ - 1][x_] == 0 and board[y_][x_ - 1] == 0:
                        dfs(x_, y_, i)
                else:
                    dfs(x_, y_, i)
    else:
        for i in range(1, 3):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and board[y_][x_] == 0:
                if i == 1:
                    if board[y_ - 1][x_] == 0 and board[y_][x_ - 1] == 0:
                        dfs(x_, y_, i)
                else:
                    dfs(x_, y_, i)


dfs(1, 0, 0)
print(rst)
