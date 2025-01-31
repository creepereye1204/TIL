n = int(input())
graph = [[10000] * n for _ in range(n)]
while True:
    a, b = map(int, input().split(" "))
    if a == -1 or b == -1:
        break
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = graph[j][i] = min(graph[i][j], graph[i][k] + graph[k][j])

mn = 100000
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
    mn = min(mn, max(graph[i]))

rst = []
for i in range(n):

    if mn == max(graph[i]):
        rst += [i + 1]
print(mn, len(rst))
print(*rst)
