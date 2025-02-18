from itertools import permutations

N, M = map(int, input().split())

l = list(map(int, input().split()))

l = list(set(map(str, l)))
l.sort()

for t in permutations(l, M):

    print(" ".join(t))
