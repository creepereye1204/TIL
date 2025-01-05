import copy

n, m = map(int, input().split(" "))

table = [list(input()) for _ in range(n)]
temp = copy.deepcopy(table)
ans = []


def solve(y, x):
    global m, n, ans
    cnt = 0
    xp = x
    yp = y
    xm = x
    ym = y
    for _ in range(1, 22):
        xp += 1
        xm -= 1
        yp += 1
        ym -= 1

        if (
            xp < m
            and yp < n
            and 0 <= ym
            and 0 <= xm
            and table[yp][x] == "*"
            and table[ym][x] == "*"
            and table[y][xp] == "*"
            and table[y][xm] == "*"
        ):

            temp[ym][x] = "."
            temp[yp][x] = "."
            temp[y][xp] = "."
            temp[y][xm] = "."
            cnt += 1

        else:

            break
    if cnt > 0:
        temp[y][x] = "."
        ans.append(str(y + 1) + " " + str(x + 1) + " " + str(cnt))


for i in range(n):
    for j in range(m):
        if table[i][j] == "*":
            solve(i, j)

for i in range(n):
    for j in range(m):
        if temp[i][j] == "*":
            print(-1)
            exit()

print(len(ans))
for a in ans:
    print(a)
