rst = 0


def res(arr, n):
    if sum(arr) == n:
        global rst
        rst += 1
        return
    elif sum(arr) > n:
        return
    res(arr+[arr[-1]+1], n)


def solution(n):
    global rst
    for i in range(1, n+1):
        res([i], n)
    return rst
