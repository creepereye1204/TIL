from collections import deque

r, c = map(int, input().split(" "))
graph = [list(input()) for _ in range(r)]

house = None
player = None
water = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == "D":
            house = (j, i)
        if graph[i][j] == "S":
            player = (j, i)
        if graph[i][j] == "*":
            water += [(j, i)]
start = [player] + water
q = deque(start)
dist = [[0] * c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
if player == house and house and house not in water:
    print(0)
    exit()

while q:
    x, y = q.popleft()
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < c and 0 <= y_ < r:
            if graph[y][x] == "*":
                if graph[y_][x_] == "." or graph[y_][x_] == "S":
                    graph[y_][x_] = "*"
                    q += [(x_, y_)]
            elif graph[y][x] == "S":
                if graph[y_][x_] == ".":
                    graph[y_][x_] = "S"
                    dist[y_][x_] = dist[y][x] + 1
                    q += [(x_, y_)]
                elif graph[y_][x_] == "D":
                    print(dist[y][x] + 1)
                    exit()

print("KAKTUS")
