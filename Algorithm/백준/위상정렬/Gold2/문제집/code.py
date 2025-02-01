import heapq


n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
prior = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a] += [b]
    prior[b] += 1

q = [i for i in range(1, n + 1) if prior[i] == 0]


heapq.heapify(q)

rst = []

while len(rst) < n:
    node = heapq.heappop(q)
    rst += [node]
    for i in graph[node]:
        prior[i] -= 1
        if prior[i] == 0:
            heapq.heappush(q, i)
print(*rst)
