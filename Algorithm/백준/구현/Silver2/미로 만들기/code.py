from collections import deque


n = int(input())
commands = list(input())
board = [["#"] * (2 * n + 1) for _ in range(2 * n + 1)]
state = deque([0, 1, 2, 3])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
mn = [1000, 1000]
mx = [-1, -1]
x = y = n
board[n][n] = "."
for command in commands:
    if command == "F":
        index = state[0]
        x = dx[index] + x
        y = dy[index] + y
        board[y][x] = "."
    elif command == "L":
        state.rotate(1)

    else:
        state.rotate(-1)

for i in range(2 * n + 1):
    for j in range(2 * n + 1):
        if board[i][j] == ".":
            mn[0] = min(mn[0], j)
            mn[1] = min(mn[1], i)
            mx[0] = max(mx[0], j)
            mx[1] = max(mx[1], i)

for i in range(mn[1], mx[1] + 1):
    for j in range(mn[0], mx[0] + 1):
        print(board[i][j], end="")
    print()
