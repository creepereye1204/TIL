from itertools import permutations

M, N = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
rst = set()
for num in permutations(arr, N):
    rst.add(num)
for t in sorted(list(rst)):
    print(*t)
