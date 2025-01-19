# n, m = map(int, input().split())
# graph = [1] * (n + 1)
# arr = []
# for i in range(m):
#     a, b = map(int, input().split())
#     arr.append((a, b))
# arr.sort()
# for a, b in arr:
#     if graph[b] <= graph[a]:
#         graph[b] = graph[a] + 1
# print(*graph[1:])

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
priod = [0] * n
ans = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    priod[b - 1] += 1
passed = []
cnt = 1
while len(passed) != n:
    able = [i for i in range(n) if priod[i] == 0 and i not in passed]
    for a in able:
        passed += [a]
        ans[a] = cnt
        for b in graph[a + 1]:
            priod[b - 1] -= 1
    cnt += 1

print(*ans)
