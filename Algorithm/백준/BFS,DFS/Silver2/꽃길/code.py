import sys

INF = sys.maxsize

sys.setrecursionlimit(10**9)


def solve():
    global value, board, n, rst
    temp = set()
    cnt = 0
    dx = [1, -1, 0, 0, 0]
    dy = [0, 0, 1, -1, 0]
    for x, y in value:
        for i in range(5):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < n and (x_, y_) not in temp:
                temp.add((x_, y_))
                cnt += board[y_][x_]
            else:
                return
    rst = min(rst, cnt)


def dfs(index):
    global visited, value, arr
    if len(value) == 3:
        solve()
        return
    for i in range(index, n**2):

        value += [(arr[i][0], arr[i][1])]

        dfs(index + 1)

        value.pop()


n = int(input())
board = [list(map(int, input().split(" "))) for _ in range(n)]
arr = [(j, i) for j in range(n) for i in range(n)]
rst = INF
value = []
dfs(0)
print(rst)
