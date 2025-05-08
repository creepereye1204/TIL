from collections import deque


def solution(queue1, queue2):

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    a = sum(queue1)
    b = sum(queue2)
    answer = 0

    for _ in range(4*len(queue1)):
        if a == b:
            return answer
        elif a > b:
            c = queue1.popleft()
            queue2.append(c)
            b += c
            a -= c
        else:
            c = queue2.popleft()
            queue1.append(c)
            b -= c
            a += c
        answer += 1
    return answer if a == b else -1
