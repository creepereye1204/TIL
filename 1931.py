import heapq

n = int(input())
join = []
cnt = 0
flag = -1

for _ in range(n):
    start, end = map(int, input().split(" "))
    heapq.heappush(join, (end, start))

while join:
    end, start = heapq.heappop(join)
    if flag <= start:
        flag = end
        cnt += 1
print(cnt)
