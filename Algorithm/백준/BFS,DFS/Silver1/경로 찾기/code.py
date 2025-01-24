n = int(input())
graph = [[] for _ in range(n)]


def dfs(i, visited):
    for node in graph[i]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, visited)


for i in range(n):
    nums = list(map(int, input().split(" ")))
    for j in range(n):
        if nums[j] == 1:
            graph[i] += [j]
for i in range(n):
    visited = [0] * n
    dfs(i, visited)
    print(*visited)
