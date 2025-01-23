from collections import deque

x, y = map(int, input().split(" "))
q = deque([x])
visited = [-1] * 100001
visited[x] = 0
while q:
    v = q.popleft()

    if -1 < 2 * v < 100001 and (visited[v * 2] == -1 or visited[v * 2] > visited[v]):
        visited[v * 2] = visited[v]
        q += [v * 2]
    if -1 < v + 1 < 100001 and (visited[v + 1] == -1 or visited[v + 1] > visited[v] + 1):
        visited[v + 1] = visited[v] + 1
        q += [v + 1]
    if -1 < v - 1 < 100001 and (visited[v - 1] == -1 or visited[v - 1] > visited[v] + 1):
        visited[v - 1] = visited[v] + 1
        q += [v - 1]
print(visited[y])
