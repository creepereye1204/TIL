T = int(input())


def rotation(table):
    n = len(table)
    ga = [table[n // 2][i] for i in range(n)]
    ju = [table[i][i] for i in range(n)]
    se = [table[i][n // 2] for i in range(n)]
    bu = [table[i][n - i - 1] for i in range(n)]

    for i in range(n):
        table[i][i] = ga[i]
        table[i][n // 2] = ju[i]
        table[i][n - i - 1] = se[i]
        table[n // 2][n - i - 1] = bu[i]
    return table


for _ in range(T):
    n, angle = map(int, input().split(" "))
    table = [list(map(int, input().split(" "))) for _ in range(n)]
    angle //= 45
    if angle < 0:
        angle += 8

    for _ in range(angle):
        table = rotation(table)

    for t in table:
        print(" ".join(map(str, t)))
