from collections import deque

n = int(input())
arr = list(map(int, input().split()))
q = deque([])
for i in range(len(arr)):
    q += [[i + 1, arr[i]]]
while q:
    index, x = q.popleft()
    print(index, end=" ")
    if x > 0:
        q.rotate(-(x - 1))
    else:
        q.rotate(-x)
