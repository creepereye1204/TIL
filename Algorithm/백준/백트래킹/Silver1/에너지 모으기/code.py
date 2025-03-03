import sys

sys.setrecursionlimit(10**6)
rst = -1


def dfs(value, arr):
    global rst
    if len(arr) < 3:
        rst = max(rst, value)
        return
    for i in range(1, len(arr) - 1):
        dfs(value + arr[i - 1] * arr[i + 1], arr[:i] + arr[i + 1 :])


input()
dfs(0, list(map(int, input().split(" "))))
print(rst)
