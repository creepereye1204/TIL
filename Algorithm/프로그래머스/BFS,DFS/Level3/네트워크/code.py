from collections import deque


def bfs(i, computers, visited):
    cnt = 0
    q = deque([i])
    while q:
        y = q.popleft()
        for j in range(len(computers)):
            if computers[y][j] == 1 and not visited[y][j]:
                cnt = 1
                visited[y][j], visited[j][y] = True, True
                q += [j]
    return cnt


def solution(n, computers):
    answer = 0
    visited = [[False] * 200 for _ in range(200)]
    for i in range(n):
        answer += bfs(i, computers, visited)

    return answer
