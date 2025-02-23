# 일단 이다솜파와 임도연파의 개수를 딕셔너리로 저장한다
# 이후 dfs를 모든 좌표에서 7개를 만들고 세트에 넣는다
# 이후 세트이 개수 리턴
graph = [list(input()) for _ in range(5)]
visited = [[False] for _ in range(5)]
group = 3
rst = set()


def dfs(x, y, cnt, group, pos):
    global visited, rst, graph
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if cnt == 7:

        rst += 1
        for x, y in pos:
            graph[y][x] = True
        return
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < 5 and 0 <= y_ < 5 and not visited[y_][x_]:

            if graph[y_][x_] == "Y" and group > 0:

                dfs(x_, y_, cnt + 1, group - 1, pos + [[x_, y_]])

            if graph[y_][x_] == "S":
                dfs(x_, y_, cnt + 1, group, pos + [[x_, y_]])


for i in range(5):
    for j in range(5):
        if not visited[j][i]:

            dfs(j, i, 0, 3, [[j, i]])

print(rst)
