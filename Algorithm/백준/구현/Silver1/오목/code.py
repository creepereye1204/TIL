board = [list(map(str, input().split(" "))) for _ in range(19)]
n = 19
dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

for y in range(n):
    for x in range(n):
        if board[y][x] != "0":
            focus = board[y][x]
            for i in range(4):
                cnt = 1
                x_ = x + dx[i]
                y_ = y + dy[i]
                while 0 <= x_ < n and 0 <= y_ < n and board[y_][x_] == focus:
                    cnt += 1
                    if cnt == 5:

                        if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and focus == board[y - dy[i]][x - dx[i]]:
                            break
                        if 0 <= x_ + dx[i] < n and 0 <= y_ + dy[i] < n and focus == board[y_ + dy[i]][x_ + dx[i]]:
                            break
                        print(focus)
                        print(y + 1, x + 1)
                        exit(0)

                    x_ += dx[i]
                    y_ += dy[i]

print(0)
