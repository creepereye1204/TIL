import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x, y = map(int, input().split(" "))
    heapq.heappush(q, (x, y))

x, y = heapq.heappop(q)
mn_x = x
mx_y = y
rst = y - x
while q:
    x, y = heapq.heappop(q)
    if mx_y < y:
        if mx_y < x:
            rst += y - x
        else:
            rst += y - mx_y
        mn_x = x
        mx_y = y
print(rst)
