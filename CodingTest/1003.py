d = [[0] * 41, [0] * 41]
d[0][0] = 1
d[1][0] = 0

d[0][1] = 0
d[1][1] = 1
for _ in range(int(input())):
    n = int(input())
    for i in range(2, n + 1):
        d[0][i] = d[0][i - 1] + d[0][i - 2]
        d[1][i] = d[1][i - 1] + d[1][i - 2]
    print(d[0][n], d[1][n])
