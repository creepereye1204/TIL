from collections import deque

MAX = 10**5


def do_bfs(N, K):
    visited = [0] * (MAX + 1)

    q = deque([N])
    while q:
        v = q.popleft()
        if v == K:
            return visited[K]

        for o in (v - 1, v + 1, 2 * v):
            if 0 <= o <= MAX and not visited[o]:
                visited[o] = 1 + visited[v]
                q += [o]


N, K = map(int, input().split(" "))
print(do_bfs(N, K))
