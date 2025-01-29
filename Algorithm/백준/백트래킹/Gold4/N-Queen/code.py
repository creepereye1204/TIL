n = int(input())
rows = [0] * n
rst = 0


def check(x):
    for i in range(x):
        if rows[x] == rows[i] or abs(rows[x] - rows[i]) == abs(x - i):
            return False
    return True


def dfs(start):
    global rst
    if start == n:
        rst += 1
        return
    for i in range(n):
        rows[start] = i
        if check(start):
            dfs(start + 1)


dfs(0)
print(rst)
