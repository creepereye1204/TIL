def backtrack(cnt, index):
    global rst, visited, graph, n
    if cnt == n // 2:
        start = link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        rst = min(rst, abs(start - link))
        return

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            backtrack(cnt + 1, i + 1)
            visited[i] = False


n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [False] * n

rst = float("inf")

backtrack(0, 0)

print(rst)
