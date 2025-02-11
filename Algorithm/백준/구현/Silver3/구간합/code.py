from itertools import accumulate

N, M = map(int, input().split())
lst = [0] + list(accumulate(map(int, input().split())))

for _ in range(M):
    s, e = map(int, input().split())
    print(lst[e] - lst[s - 1])
