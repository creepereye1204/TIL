# 2중 포문으로 따을 찾으며 visite 처리ㅏ고 각 땅마다 고유한 안덱스 부여
# 면이 하나라도 바다랑 닿는 땅만 큐에 저장(인덱스 까지)
# 및에서 가본곳이먀면서 아래ㅔ 만족하면
# 이후 큐를 BFS를 돌리며 dist 갱신 이때 만나는 땅이 다른 인덱스 이면탐색종료
# 이때 같은 인덱스이고 가본곳이면이면 패스
from collections import deque


def check(x, y, index):
    global graph, dx, dy, n, q

    for i in range(4):
        x_ = dx[i] + x
        y_ = dy[i] + y
        if 0 <= x_ < n and 0 <= y_ < n and graph[y_][x_] == 0:
            q.append([x, y, index])
            return


def solve(x, y, index):

    temp = deque([[x, y]])
    visited[y][x] = True
    check(x, y, index)
    while temp:
        x, y = temp.popleft()
        for i in range(4):
            x_ = dx[i] + x
            y_ = dy[i] + y
            if 0 <= x_ < n and 0 <= y_ < n and graph[y_][x_] == 1 and not visited[y_][x_]:
                temp.append([x_, y_])
                visited[y_][x_] = True
                check(x_, y_, index)


n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist = [[-1] * n for _ in range(n)]
index = 2
# 찾은 땅마다 dist 0으로 초기화

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:

            solve(j, i, index)
            index += 1
