import sys

sys.setrecursionlimit(10**9)


def dfs(index, value):
    global arr, m, rst
    if len(value) == m and value not in rst:
        rst += [value]
        print(*value)
        return
    for i in range(index, len(arr)):

        dfs(i + 1, value + [arr[i]])


n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

rst = []
dfs(0, [])
