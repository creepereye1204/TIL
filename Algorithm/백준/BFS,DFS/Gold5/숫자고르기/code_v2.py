n = int(input())
result = []
graph = [0] + [int(input()) for _ in range(n)]


def dfs(start, end):
    global visited, graph, result
    if start == end and end in visited:
        result.append(start)
    elif len(visited) < n:
        visited += [start]
        dfs(start, graph[end])


for i in range(1, n + 1):
    visited = []
    dfs(i, i)

print(len(result))

for i in sorted(result):
    print(i)
