from heapq import heappop, heappush

def solution(n, k, enemy):
    sumEnemy = 0
    heap = []
    
    for idx,e in enumerate(enemy):
        heappush(heap,-e)
        sumEnemy+=e
        if sumEnemy>n:
            if k==0:
                return idx
            sumEnemy+=heappop(heap)
            k-=1
    return len(enemy)