mx = -1

n = int(input())
table = [list(input()) for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if table[i][j] == "Y" and i != j:
            graph[i] += [j]
            graph[j] += [i]


def bfs(i):
    global mx
    visited = [i]
    q = []
    for node in graph[i]:
        if node not in visited:
            visited += [node]
            q += [node]

    for i in q:
        for node in graph[i]:
            if node not in visited:
                visited += [node]
    mx = max(mx, len(visited) - 1)


for i in range(n):
    bfs(i)

print(mx)
