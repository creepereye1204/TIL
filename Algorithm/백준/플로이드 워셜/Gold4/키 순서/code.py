rst = 0
N, M = map(int, input().split(" "))
students = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    students[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if students[i][k] + students[k][j] == 2:
                students[i][j] = 1


for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        cnt += students[i][j] + students[j][i]
    if cnt == N - 1:
        rst += 1
print(rst)
