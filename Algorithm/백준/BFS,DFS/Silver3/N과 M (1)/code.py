N, M = map(int, input().split(" "))
visited = [False] * N
n = list(range(1, N + 1))


def dfs(arr, cnt):
    global M, n, visited
    if cnt == M:
        print(*arr)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(arr + [n[i]], cnt + 1)
            visited[i] = False


dfs([], 0)
