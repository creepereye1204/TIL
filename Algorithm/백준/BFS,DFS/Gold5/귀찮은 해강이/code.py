# cur 변수에 현 그룹의 set을 저장 (처음에는 처음순서 그룹으로 설정)
# 함수를 만듬 기능은 현재 그룹안에 원하는 번호가있는지 확인하고 없으면 카운트+1 하고 cur를 다른 그룹으로 바꾸어줌
# 이걸 n번 반복해


# 1 처음에 그래프를 만들어

# 여기서qnxj n 시간 걸림


# 이후 그래프의 그룹을 순회하면서

# 그래프_콘버터 리스트는 각 점수에 따른 값을 저장해
# 두번째_콘버터 리스트는 각 점수에 해당하는 그룹을저장해

# 값이 들어올때마다 위 행위로 최대 2n 시간 그리고 3n*4바이트 메모리를 사용
from collections import deque

n, m = map(int, input().split(" "))
graph = [[] for _ in range(1 + n)]
visited = set()

table_1 = [i for i in range(n + 1)]
table_2 = [set() for i in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a] += [b]
    graph[b] += [a]


def bfs(index, i):
    global table_1, table_2, visited
    q = deque([index])
    visited.add(index)
    table_1[index] = i
    table_2[i].add(index)
    while q:
        v = q.popleft()
        for node in graph[v]:
            if node not in visited:
                q += [node]
                table_1[node] = i
                table_2[i].add(node)
                visited.add(node)


def solve(index):
    global cur, cnt
    if index not in cur:
        cnt += 1
        cur = table_2[table_1[index]]


for i in range(1, n + 1):
    if i not in visited:
        bfs(i, i)

qna = list(map(int, input().split()))
cnt = 0
cur = table_2[table_1[qna[0]]]
for index in qna[1:]:
    solve(index)

print(cnt)
