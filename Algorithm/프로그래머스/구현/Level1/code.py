def solution(n, lost, reserve):
    ans = 0
    A = list(set(lost) - set(reserve))
    B = list(set(reserve) - set(lost))
    arr = [False] * (n + 2)
    for b in B:
        arr[b] = True
    A.sort()
    for a in A:
        if arr[a - 1]:
            arr[a - 1] = False
            ans += 1
        elif arr[a + 1]:
            arr[a + 1] = False
            ans += 1

    return n - len(A) + ans
