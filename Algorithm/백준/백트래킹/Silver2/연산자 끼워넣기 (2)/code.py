import sys

sys.setrecursionlimit(10**6)
mn = sys.maxsize
mx = -sys.maxsize
n = int(input())
arr = list(map(int, input().split(" ")))
op = list(map(int, input().split(" ")))


def calc(value, i, num):
    global op
    if i == 0:
        return value + num
    elif i == 1:
        return value - num
    elif i == 2:
        return value * num
    else:
        if value >= 0:
            return value // num
        return -(-value // num)


def dfs(index, value):
    global n, mx, mn, op, arr
    if index == n:
        mn = min(mn, value)
        mx = max(mx, value)
        return

    for i in range(4):
        if op[i] > 0:
            y = calc(value, i, arr[index])
            op[i] -= 1
            dfs(index + 1, y)
            op[i] += 1


dfs(1, arr[0])
print(mx)
print(mn)
