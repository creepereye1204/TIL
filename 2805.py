n, m = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))

MIN, MAX = 1, max(trees)

while MIN <= MAX:
    log = 0
    mid = (MIN + MAX) // 2
    for tree in trees:
        if mid < tree:
            log += tree - mid
    if log >= m:
        MIN = mid + 1

    else:
        MAX = mid - 1
print(MAX)
