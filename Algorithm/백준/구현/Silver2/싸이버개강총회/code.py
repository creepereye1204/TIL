from collections import deque

import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    start = []
    end = []
    mx = -1
    for i in range(n):
        if i % 2 == 1:
            start.append(arr[i])
        else:
            end.append(arr[i])
    q = deque(start + end[::-1])
    for _ in range(n - 1):
        mx = max(mx, abs(q[0] - q[1]), abs(q[1] - q[2]))
        q.rotate(1)
    print(mx)
