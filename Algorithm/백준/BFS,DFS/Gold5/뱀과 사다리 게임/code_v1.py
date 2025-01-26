from collections import deque


table = [-1] * 101
mn = 1000000000000
plus, minus = map(int, input().split(" "))
for _ in range(plus + minus):
    x, y = map(int, input().split(" "))
    table[x] = y

q = deque([[1, 0]])
visited = [1000000000] * 101
while q:
    node, cnt = q.popleft()
    if node == 100:
        mn = min(mn, cnt)
        continue
    if table[node] != -1:
        q += [[table[node], cnt]]
        continue
    cnt += 1
    for i in range(6, 0, -1):
        y = i + node
        if y < 101 and visited[y] > cnt:
            visited[y] = cnt
            q += [[y, cnt]]
print(mn)
