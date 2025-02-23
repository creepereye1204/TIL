r, c, n = map(int, input().split(" "))
graph = [list(input()) for _ in range(r)]


def rollback(graph):
    global r, c
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                graph[i][j] = "."
            else:
                graph[i][j] = "O"


def run(graph, x, y):
    global r, c
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[y][x] = "X"
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < c and 0 <= y_ < r and graph[y_][x_] == ".":
            graph[y_][x_] = "X"


if n % 2 == 0:
    for i in range(r):
        for j in range(c):
            print("O", end="")
        print()
    exit(0)
else:
    for _ in range(n // 2):
        for i in range(r):
            for j in range(c):
                if graph[i][j] == "O":
                    run(graph, j, i)
        rollback(graph)

for i in range(r):
    for j in range(c):
        print(graph[i][j], end="")
    print()
