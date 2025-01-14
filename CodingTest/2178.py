from collections import deque

N, M = map(int, input().split(" "))
graph = [list(map(int, list(input()))) for _ in range(N)]

q = deque([[0, 0]])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y = q.popleft()

    if x == M - 1 and y == N - 1:
        print(graph[N - 1][M - 1])

        exit(0)
    for i in range(4):
        x_ = dx[i] + x
        y_ = dy[i] + y
        if 0 <= x_ < M and 0 <= y_ < N and graph[y_][x_] == 1:
            graph[y_][x_] = graph[y][x] + 1
            q += [[x_, y_]]
