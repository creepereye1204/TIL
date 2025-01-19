from collections import deque

node = int(input())
edge = int(input())
graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    a, b = map(int, input().split(" "))
    graph[a] += [b]
    graph[b] += [a]


def solution(graph):
    visited = [1]
    q = deque([1])
    while q:
        node = q.popleft()
        for n in graph[node]:
            if n not in visited:
                visited += [n]
                q += [n]

    answer = len(visited) - 1
    return answer


print(solution(graph))
