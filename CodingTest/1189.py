r, c, k = map(int, input().split(" "))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
visited[r - 1][0] = True


def dfs(x, y, cnt):
    global result, visited
    if cnt == k and x == c - 1 and y == 0:
        result += 1
        return
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < c and 0 <= y_ < r and not visited[y_][x_] and graph[y_][x_] != "T":
            visited[y_][x_] = True
            dfs(x_, y_, cnt + 1)
            visited[y_][x_] = False


if graph[r - 1][0] != "T":
    dfs(0, r - 1, 1)
print(result)
