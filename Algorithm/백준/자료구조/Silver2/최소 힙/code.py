import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    m = int(input())
    if m == 0 and arr:
        print(heapq.heappop(arr))
    elif m == 0 and not arr:
        print(0)
    else:
        heapq.heappush(arr, m)
