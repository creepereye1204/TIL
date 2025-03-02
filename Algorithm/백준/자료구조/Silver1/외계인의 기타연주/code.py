# 만약에 뽑은 수보다 크면 카운트1 그후 담기
# 작으면 빼고 카운트 1 그리고 계속 반복
# 같으면 카운트 X 패스
import heapq
import sys

input = sys.stdin.readline


def solution(r, c):
    rst = 0
    arrs = [[] for _ in range(6)]
    for i in range(r):
        a, b = map(int, input().split(" "))
        if not arrs[a - 1]:
            heapq.heappush(arrs[a - 1], -b)
            rst += 1
        else:
            while arrs[a - 1]:
                x = -heapq.heappop(arrs[a - 1])
                if x < b:
                    rst += 1
                    heapq.heappush(arrs[a - 1], -b)
                    heapq.heappush(arrs[a - 1], -x)
                    break
                elif x > b:
                    rst += 1
                else:
                    heapq.heappush(arrs[a - 1], -x)
                    break
            else:
                heapq.heappush(arrs[a - 1], -b)
                rst += 1
    return rst


print(solution(*map(int, input().split(" "))))
