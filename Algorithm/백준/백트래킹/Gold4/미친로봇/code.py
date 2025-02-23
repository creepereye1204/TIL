dansun = 0

n, *dirs = map(int, input().split(" "))
visited = [[False] * (2 * n + 1) for _ in range(2 * n + 1)]
visited[n][n] = True


def dfs(j, i, cnt, percent):
    global dansun, n, visited, dirs

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if cnt == n:
        dansun += percent
        return
    for index in range(4):
        x = j + dx[index]
        y = i + dy[index]
        if 0 <= x < (2 * n + 1) and 0 <= y < (2 * n + 1):

            if not visited[y][x]:
                visited[y][x] = True

                dfs(x, y, cnt + 1, percent * (dirs[index] / 100))
                visited[y][x] = False


dfs(n, n, 0, 1)
print(dansun)
