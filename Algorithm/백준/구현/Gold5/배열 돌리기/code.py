import copy

n, m, r = map(int, input().split(" "))
table = [list(map(int, input().split(" "))) for _ in range(n)]


def rotate_table():
    global table
    temp = copy.deepcopy(table)

    for i in range(n):
        for j in range(m):
            v = temp[i][j]
            try:
                table[i][j - 1] = v
            except:
                try:
                    table[i + 1][j] = v
                except:
                    try:
                        table[i][j + 1] = v
                    except:
                        table[i - 1][j] = v


for _ in range(r):
    rotate_table()
for t in table:
    print(*t)
