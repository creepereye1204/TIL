import sys

input = sys.stdin.readline


def Union(a, b):
    a = Find(a)
    b = Find(b)
    if a == b:
        return
    if a < b:
        disjoint[b] = a
    else:
        disjoint[a] = b


def Find(x):
    if x != disjoint[x]:
        disjoint[x] = Find(disjoint[x])

    return disjoint[x]


N, M = map(int, input().split())

disjoint = [0] * (N + 1)

for i in range(1, N + 1):
    disjoint[i] = i


for i in range(M):

    a, b = map(int, input().split())
    Union(a, b)

L = list(map(int, input().split()))
total = 0
for i in range(1, len(L)):

    if Find(L[i - 1]) != Find(L[i]):
        total += 1

print(total)
