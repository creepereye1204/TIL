from collections import deque


def solution(priorities, location):
    q = deque([[prioritie, idx] for idx, prioritie in enumerate(priorities)])
    l = len(q)
    mx = -1
    while q:
        mx = max(list(zip(*q))[0])
        v, idx = q.popleft()
        if v < mx:
            q += [[v, idx]]
        else:
            if idx == location:
                return l - len(q)
