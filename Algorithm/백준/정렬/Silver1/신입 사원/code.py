from collections import deque
import sys

INF = sys.maxsize
T = int(input())
for i in range(T):  # 20번
    n = int(input())
    arr = []
    for j in range(n):  # 10만번
        a, b = map(int, input().split(" "))
        arr += [[a, b]]
    arr.sort(key=lambda x: (x[0]))
    cnt = 0
    arr = deque(arr)
    mx = INF
    while arr:  # 10만번
        _, y = arr.popleft()
        if mx > y:
            cnt += 1
            mx = y
    print(cnt)
