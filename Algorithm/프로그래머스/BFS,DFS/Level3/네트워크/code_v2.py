from collections import deque


visited = []


def bfs(i, computers):
    global visited
    q = deque([i])
    while q:
        y = q.popleft()
        for j in range(len(computers)):
            if computers[y][j] == 1 and j not in visited:
                visited += [j]
                q += [j]


def solution(n, computers):
    answer = 0
    global visited
    for i in range(n):
        if i not in visited:
            bfs(i, computers)
            answer += 1
    return answer
