import sys
from collections import deque

INF = sys.maxsize

input()
arr = list(map(int, input().split(" ")))
n = max(arr) + 1
dp = [[[INF] * n for _ in range(n)] for _ in range(n)]
if len(arr) == 1:
    arr += [0]
    arr += [0]
elif len(arr) == 2:
    arr += [0]

z, y, x = arr[0], arr[1], arr[2]
dz = [9, 9, 3, 3, 1, 1]
dy = [3, 1, 9, 1, 3, 9]
dx = [1, 3, 1, 9, 9, 3]
dp[arr[0]][arr[1]][arr[2]] = 1
q = deque([(x, y, z)])
while q:
    x, y, z = q.popleft()
    if z == 0 and y == 0 and x == 0:
        print(dp[0][0][0] - 1)
        exit()
    for i in range(len(dx)):
        z_ = z - dz[i]
        y_ = y - dy[i]
        x_ = x - dx[i]
        z_ = z_ if z_ >= 0 else 0
        y_ = y_ if y_ >= 0 else 0
        x_ = x_ if x_ >= 0 else 0
        if dp[z_][y_][x_] == INF:
            dp[z_][y_][x_] = min(dp[z][y][x] + 1, dp[z_][y_][x_])

            q.append((x_, y_, z_))
