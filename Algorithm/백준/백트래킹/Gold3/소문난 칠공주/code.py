from collections import deque

rst = 0
board = [list(input()) for _ in range(5)]
graph = [[j, i] for j in range(5) for i in range(5)]
s = []


def dfs(index, cnt):  # 백트래킹으로 좌표 조합 찾기
    global rst, graph, board, s

    if len(s) == 7:

        if bfs(s):
            rst += 1
        return
    for i in range(index, 25):
        s = s + [graph[i]]
        if board[graph[i][1]][graph[i][0]] == "Y" and cnt > 0:
            dfs(i + 1, cnt - 1)

        if board[graph[i][1]][graph[i][0]] == "S":
            dfs(i + 1, cnt)
        s.pop()


def bfs(s):  # 찾을떄마다 검증하기
    global board
    l = [i for i in s]
    q = deque([l[0]])
    l.remove(l[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if [x_, y_] in l:

                q += [[x_, y_]]
                l.remove([x_, y_])

    if l:
        return False
    return True


dfs(0, 3)
print(rst)
