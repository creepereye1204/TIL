import sys

sys.setrecursionlimit(10**6)
rst = -1
limit = 0
arr = []
visited = []
n = 0


def dfs(value):
    global rst, limit, arr, visited, n
    if value != "" and int(value) >= limit:
        return
    if all(visited) and len(str(int(value))) == n:
        rst = max(int(value), rst)
        return
    else:

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(value + arr[i])
                visited[i] = False


def solution(num1, num2):
    global limit, arr, visited, n
    arr = num1
    limit = int(num2)
    n = len(num1)
    visited = [False] * n
    dfs("")
    return rst


a, b = map(str, input().split(" "))

print(solution(a, b))
