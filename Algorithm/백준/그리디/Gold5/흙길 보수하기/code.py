# 힙으로 웅덩이의 시작지점이 작은 순으로 뽑는다

# 이후 테이프의 위치가 끝지점보다 크다면 pass
# 아니라면 뽑은 시작이 테이프이 취치보다 작으면 뽑은 시작부터 테이프질
# 아니라면 현재 위,치에서 테이프질
import heapq

n, l = map(int, input().split())
q = []
rst = 0
cur = 0
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (start, end))
while q:
    start, end = heapq.heappop(q)

    if cur < end:
        temp = 0
        if start > cur:
            cur = start
        temp = int((end - cur) // l)
        if (end - cur) % l != 0:
            temp += 1

        rst += temp
        cur += temp * l


print(rst)
