from collections import deque

answer = 0
n = int(input())
q1 = deque()

for i in range(n * 2):
    if i < n:
        q1 += [input()]
    else:
        out = input()
        if out != q1[0]:
            q1.remove(out)
            answer += 1
        else:
            q1.popleft()
print(answer)
