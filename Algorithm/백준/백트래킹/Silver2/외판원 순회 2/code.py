import sys

sys.setrecursionlimit(10**9)
n = int(input())
visited = [False] * n
rst = sys.maxsize
graph = [list(map(int, input().split(" "))) for _ in range(n)]


def dfs(value, num, now):
    global visited, n, rst, graph
    if all(v for v in visited):
        if graph[num][now] != 0:
            rst = min(rst, value + graph[num][now])

        return
    for i in range(n):
        if not visited[i] and graph[num][i] != 0:
            visited[i] = True
            dfs(value + graph[num][i], i, now)
            visited[i] = False


for i in range(n):

    visited[i] = True
    dfs(0, i, i)
    visited[i] = False
print(rst)
