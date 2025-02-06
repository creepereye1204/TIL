from collections import deque


table = [-1] * 101
plus, minus = map(int, input().split(" "))
for _ in range(plus + minus):
    x, y = map(int, input().split(" "))
    table[x] = y

q = deque([1])
visited = [0] * 101
while q:
    now = q.popleft()
    if now == 100:
        print(visited[100])
        exit(0)
    for i in range(6, 0, -1):
        y = i + now
        if y < 101 and visited[y] == 0:
            visited[y] = visited[now] + 1
            if table[y] == -1:
                q += [y]
            else:
                q += [table[y]]
