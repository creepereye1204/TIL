import heapq


def solution(x):
    heap = []
    for _ in range(x):

        n = int(input())
        if n == 0:
            try:
                print(heapq.heappop(heap))
            except IndexError:
                print(0)
        else:
            heapq.heappush(heap, n)


solution(int(input()))
