from collections import deque

n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
result = []


def bfs():
    global result
    q = deque([[a] for a in arr])
    while q:
        v = q.popleft()
        if len(v) == m:
            result += [v] if v not in result else []
            continue
        for a in arr:
            if v[-1] <= a:
                q += [v + [a]]


bfs()
for r in sorted(result):
    print(" ".join(list(map(str, r))))
