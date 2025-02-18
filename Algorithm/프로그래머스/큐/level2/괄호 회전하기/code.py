# 스택으로 차곡차곡 쌓다가 '(' 나오면 팦 근데 스택이 비ㅓ있으면 실패
# 혹은 s다뽑았는데 스택이 남았으면 실패
# 스택이 비어있으면 성공!
from collections import deque


def solution(s):
    t = {"{": "}", "[": "]", "(": ")"}
    q = deque(list(s))
    answer = 0
    for i in range(len(s)):
        temp = q.copy()
        temp.rotate(-i)
        flage = False
        stack = []
        while temp:
            v = temp.popleft()
            if v in ["{", "[", "("]:
                stack += v
            else:
                if stack and t[stack[-1]] == v:
                    stack.pop()
                else:
                    flage = True
                    break

        if not flage and not stack:
            answer += 1

    return answer
