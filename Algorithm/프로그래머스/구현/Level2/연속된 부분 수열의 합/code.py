from collections import deque


def solution(sequence, k):
    answer = []
    queue = deque()
    s = 0
    for i in range(len(sequence)):
        queue.append(i)
        s += sequence[i]
        while queue and k < s:
            s -= sequence[queue.popleft()]
        if s == k:
            answer.append([queue[0], queue[-1]])
    answer.sort(key=lambda x: (x[1]-x[0]))
    return answer[0]
