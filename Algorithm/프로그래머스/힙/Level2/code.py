import heapq


def solution(scoville, K):

    heapq.heapify(scoville)
    cnt = 0
    while scoville:

        try:

            a = heapq.heappop(scoville)
            if a >= K:
                return cnt
            b = heapq.heappop(scoville)

            if a < K or b < K:
                c = a + 2 * b
                cnt += 1
                heapq.heappush(scoville, c)

        except:
            return -1


scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville, K))
