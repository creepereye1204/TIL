from collections import deque
import sys

input = sys.stdin.readline


def bfs(y, x, df, visited, M, N):
    q = deque([(x, y)])  # 튜플 사용
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    visited[y][x] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            x_ = x + dx[i]
            y_ = y + dy[i]
            if 0 <= x_ < M and 0 <= y_ < N and not visited[y_][x_] and df[y_][x_]:
                q.append((x_, y_))  # 튜플 사용
                visited[y_][x_] = True


def solution(M, N, K):
    cnt = 0
    df = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]  # 단순 초기화

    for _ in range(K):
        x, y = map(int, input().split(" "))
        df[y][x] = True

    for i in range(N):
        for j in range(M):
            if df[i][j] and not visited[i][j]:
                bfs(i, j, df, visited, M, N)
                cnt += 1
    print(cnt)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split(" "))
    solution(M, N, K)
