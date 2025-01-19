from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(v):
    q = deque([v])

    visited_list1[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited_list1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited_list1[i] = 1


def dfs(v):
    visited_list2[v] = 1
    print(v, end=" ")
    for i in range(1, n + 1):
        if visited_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int, input().split(" "))
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited_list1 = [0] * (n + 1)
visited_list2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
