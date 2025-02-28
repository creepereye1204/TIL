from collections import deque

sea = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check(x, y):
    global visited, graph, sea, dx, dy, r, c
    cnt = 0
    for i in range(4):
        x_ = dx[i] + x
        y_ = dy[i] + y
        if 0 <= x_ < c and 0 <= y_ < r:
            if graph[y_][x_] == ".":
                cnt += 1
        else:
            cnt += 1
    if 3 <= cnt <= 4:
        sea.append([x, y])


def bfs(x, y):
    global visited, graph, sea, dx, dy
    q = deque([[x, y]])
    visited[y][x] = True
    check(x, y)

    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = dx[i] + x
            y_ = dy[i] + y
            if 0 <= x_ < c and 0 <= y_ < r and graph[y_][x_] == "X" and not visited[y_][x_]:
                visited[y_][x_] = True
                q.append([x_, y_])
                check(x_, y_)


def solution(r, c, graph):
    # 땅이 있는 곳을 for문으로 찾고 bfs를 사용하여 순회하되 이때 체크 함수로 잠길곳인지 판단.
    # 전부 착도나서 나중에 땅들을 바꿔주고 이떄 다시 땅들의 최저 최고 좌표를 찾은다음 그래프 다시
    # 그리기

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X" and not visited[i][j]:
                bfs(j, i)
    for x, y in sea:
        graph[y][x] = "."

    mx = [-1, -1]
    mn = [55, 55]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                mx[0] = max(mx[0], j)
                mx[1] = max(mx[1], i)
                mn[0] = min(mn[0], j)
                mn[1] = min(mn[1], i)
    rst = [[graph[i][j] for j in range(mn[0], mx[0] + 1)] for i in range(mn[1], mx[1] + 1)]
    return rst


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
result = solution(r, c, graph)
for r in result:
    print("".join(r))
