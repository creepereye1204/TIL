import math
import sys

sys.setrecursionlimit(10 * 8)
n = int(input())
arr = []
visited = [False] * n
rst = sys.maxsize
for _ in range(n):
    a, b = map(int, input().split(" "))
    arr += [[a, b]]


def dfs(index, value):
    global visited, arr, rst, n
    if any(visited):
        x = math.prod(list(zip(*value))[0])
        y = sum(list(zip(*value))[1])
        rst = min(rst, abs(x - y))

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, value + [arr[i]])
            visited[i] = False


dfs(0, [])
print(rst)
