def solution(value, op):
    global cnt, arr
    if value == n:
        cnt += 1
        if cnt == k:
            print(op[1:])
            exit(0)
        return
    elif value > n:
        return

    for a in arr:
        solution(value + a, op + "+" + str(a))


n, k = map(int, input().split(" "))
arr = [1, 2, 3]
cnt = 0
solution(0, "")
print(-1)
