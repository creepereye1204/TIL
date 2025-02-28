import sys

sys.setrecursionlimit(10**6)


n, m = map(int, input().split(" "))
arr = list(set(map(int, input().split(" "))))
value = []
arr.sort()
rst = []


def dfs(cnt):
    global value
    if cnt == m:

        print(" ".join(map(str, value)))

        return

    for a in arr:
        value.append(a)
        dfs(cnt + 1)
        value.pop()


dfs(0)
