from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    while A and B:
        a = A.popleft()
        while B and a >= B[0]:
            B.popleft()

        if not B:
            break

        else:
            B.popleft()
            answer += 1

    return answer
