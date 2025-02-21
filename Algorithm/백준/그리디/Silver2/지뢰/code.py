# 백준 2232
import sys

n = int(sys.stdin.readline())
lst = []
lst.append(0)
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.append(0)
ans = []
for i in range(1, n + 1):
    if lst[i - 1] <= lst[i] and lst[i] >= lst[i + 1]:
        ans.append(i)
for i in ans:
    print(i)
