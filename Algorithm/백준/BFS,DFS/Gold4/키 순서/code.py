from collections import deque, Counter

rst = 0
tree = []
dd = []


def bfs(i, graph, n):

    q = deque([i])
    dist = [0] * (n + 1)
    while q:
        v = q.popleft()

        for node in graph[v]:

            dist[node] = dist[v] + 1
            q += [node]

    return len([d for d in dist if d != 0]), max(dist)


n, m = map(int, input().split(" "))

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a] += [b]

for i in range(1, n + 1):
    cnt, depth = bfs(i, graph, n + 1)
    dd += [[depth, cnt]]
    tree += [depth]
# print(tree)
counter = Counter(tree)
for key, value in counter.items():
    cnt = 0
    if value == 1:
        for key_, value_ in dd:
            if key_ < key:
                cnt += 1
print(cnt)
