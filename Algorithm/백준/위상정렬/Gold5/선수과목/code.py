n, m = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
prior = [0] * (n + 1)
rst = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a] += [b]
    prior[b] += 1


passed = set([])
grade = 1
while len(passed) != n:
    able = [i for i in range(1, n + 1) if prior[i] == 0 and i not in passed]
    for a in able:
        rst[a] = grade
        passed.add(a)
        for b in graph[a]:
            prior[b] -= 1
    grade += 1
print(*rst[1:])
