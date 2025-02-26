import sys

sys.setrecursionlimit(10**9)
n = int(input())
arr = list(map(int, input().split(" ")))
visited = [False] * n
rst = -sys.maxsize


def sol(value):
    global n
    temp = 0
    for i in range(n - 1):
        temp += abs(value[i] - value[i + 1])
    return temp


def dfs(value):
    global visited, arr, rst, n
    if all(visited):
        rst = max(rst, sol(value))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(value + [arr[i]])
            visited[i] = False


dfs([])
print(rst)
