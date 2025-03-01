n = int(input())
target = int(input())
table = [[0] * n for _ in range(n)]
x = y = n // 2
dx = []
dy = []
op = -1
cnt = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        dx.append(op * cnt)
    else:
        dx.append(0)
        op = -op
        cnt += 1
op = -1
cnt = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        dy.append(op * cnt)
    else:
        dy.append(0)
        cnt += 1
        op = -op
for i in range(n):
    for j in range