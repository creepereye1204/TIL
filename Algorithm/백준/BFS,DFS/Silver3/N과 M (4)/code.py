n, m = map(int, input().split(" "))
arr = list(range(1, n + 1))


def dfs(index, cnt, value):
    if cnt == m:
        print(*value)
        return
    for i in range(index, n):
        dfs(i, cnt + 1, value + [arr[i]])


dfs(0, 0, [])
