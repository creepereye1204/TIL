INF = int(1e9)
city = int(input()) + 1
bus = int(input())
graph = [[INF] * city for _ in range(city)]

for i in range(1, city):
    for j in range(1, city):
        if i == j:
            graph[i][j] = 0

for _ in range(bus):
    a, b, c = map(int, input().split(" "))
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, city):
    for i in range(1, city):
        for j in range(1, city):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, city):
    for j in range(1, city):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print("")
