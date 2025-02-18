from collections import deque


def bfs(nodes, r, c, graph):
    q = deque(nodes)
    dist = [[-1] * c for _ in range(r)]
    dist[nodes[0][1]][nodes[0][0]] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        if graph[y][x] == "J":
            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < c and 0 <= y_ < r and dist[y_][x_] == -1 and graph[y_][x_] == ".":
                    dist[y_][x_] = dist[y][x] + 1
                    graph[y_][x_] = "J"
                    q += [[x_, y_]]
                elif x_ < 0 or y_ < 0 or c <= x_ or r <= y_:
                    print(dist[y][x] + 1)
                    exit(0)

        else:

            for i in range(4):
                x_ = x + dx[i]
                y_ = y + dy[i]
                if 0 <= x_ < c and 0 <= y_ < r and (graph[y_][x_] == "J" or graph[y_][x_] == "."):
                    graph[y_][x_] = "F"
                    q += [[x_, y_]]
    print("IMPOSSIBLE")
    exit(0)


r, c = map(int, input().split(" "))
graph = [list(input()) for _ in range(r)]
x1 = y1 = 0
fires = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            x1 = j
            y1 = i
        if graph[i][j] == "F":
            fires += [[j, i]]
bfs([[x1, y1]] + fires, r, c, graph)
