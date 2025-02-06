mx = -1111111111111
mn = 1111111111111


def solve(arr, cnt):

    for a in arr:
        if int(a) % 2 == 1:
            cnt += 1

    if len(arr) == 1:
        global mx, mn
        mx = max(cnt, mx)
        mn = min(mn, cnt)
        return
    elif len(arr) == 2:
        temp = str(int(arr[1]) + int(arr[0]))
        solve(temp, cnt)
    else:
        for i in range(1, len(arr)):
            for j in range(i + 1, len(arr)):

                temp = str(int(arr[:i]) + int(arr[i:j]) + int(arr[j:]))
                solve(temp, cnt)


solve(input(), 0)
print(mn, mx)
