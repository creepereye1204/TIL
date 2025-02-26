n, m = map(int, input().split())
rst = 0
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]


def solve(x, y):
    global rst
    for i in range(y, y + 3):
        for j in range(x, x + 3):

            A[i][j] = abs(A[i][j] - 1)


if (m < 3 or n < 3) and A != B:
    print(-1)
    exit(0)
else:
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                solve(j, i)
                rst += 1
if A != B:
    print(-1)
else:
    print(rst)
