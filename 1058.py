from collections import deque


mx = -1


def bfs(graph, i):
    global mx
    cnt = 0
    visited = [i]
    q = deque([i])
    while q:
        v = q.popleft()
        for node in graph[v]:

            if node not in visited:
                visited += [node]
                cnt += 1
                q += [node]
    mx = max(cnt, mx)


n = int(input())
graph = [[] for _ in range(n)]
for j in range(n):
    text = input()
    for i in range(len(text)):
        if text[i] == "Y":
            graph[i] += [j]
            graph[j] += [i]

for i in range(n):
    bfs(graph, i)
print(mx)
