n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
start, end = 0, max(arr)
rst = 0


def divide(mid):
    cnt = 1
    mx = mn = arr[0]
    for i in range(n):
        mx = max(mx, arr[i])
        mn = min(mn, arr[i])
        if mx - mn > mid:
            cnt += 1
            mx = mn = arr[i]
    return cnt <= m


while start <= end:
    mid = (start + end) // 2
    if divide(mid):
        end = mid - 1
        rst = mid
    else:
        start = mid + 1

print(rst)
