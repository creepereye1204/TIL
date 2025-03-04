from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in visited:
                visited.add(node)
                queue.append(node)

    return len(visited)


def solution(n, wires):
    answer = n  # 최대 송전탑 수는 n이므로 초기값을 n으로 설정

    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]

        # i번째 간선을 제외한 그래프 생성
        for j in range(len(wires)):
            if j != i:
                a, b = wires[j]
                graph[a].append(b)
                graph[b].append(a)

        visited = set()
        # 첫 번째 송전탑에서 BFS 시작
        cnt = bfs(graph, wires[0][0], visited)

        # 두 번째 송전탑의 개수는 n - cnt
        other_cnt = n - cnt
        # 송전탑 개수 차이 계산
        answer = min(answer, abs(cnt - other_cnt))

    return answer
