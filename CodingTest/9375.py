from collections import defaultdict

T = int(input())
for _ in range(T):
    result = 1
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        value, category = input().split(" ")
        d[category] += [value]
    for key in d.keys():
        result *= len(d[key]) + 1
    print(result - 1)
