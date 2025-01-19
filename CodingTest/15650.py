N, M = map(int, input().split())

from itertools import combinations

for seq in combinations([i for i in range(1, N + 1)], M):
    print(*seq)
