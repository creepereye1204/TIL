import heapq
def solution(n, works):
    answer = 0
    q=[]
    for work in works:
        heapq.heappush(q,-work)
    for _ in range(n):
        work=heapq.heappop(q)
        heapq.heappush(q,work+1)
    for i in q:
        if i<0:
            answer+=i**2
    return answer