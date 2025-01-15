from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    x: int
    y: int


def bfs():
    N, M = map(int, input().split(" "))
    graph = [list(input()) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    x, y = 0, 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "I":
                x, y = j, i
                visited[y][x] = True
                break

    q = deque([Node(x, y)])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    while q:
        node = q.popleft()
        x, y = node.x, node.y
        for i in range(4):
            temp_x = dx[i] + x
            temp_y = dy[i] + y
            if 0 <= temp_x < M and 0 <= temp_y < N and graph[temp_y][temp_x] != "X" and not visited[temp_y][temp_x]:
                visited[temp_y][temp_x] = True
                if graph[temp_y][temp_x] == "P":
                    cnt += 1
                q += [Node(temp_x, temp_y)]
    return cnt if cnt > 0 else "TT"


print(bfs())
