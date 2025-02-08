import sys

k = int(input())
nodes = list(map(int, input().split()))
results = [[] for _ in range(k)]


def solve(start, end, depth):
    global results
    center = (start + end) // 2
    if start == end:
        results[depth] += [nodes[start]]
        return

    results[depth] += [nodes[center]]
    solve(start, center - 1, depth + 1)
    solve(center + 1, end, depth + 1)


solve(0, len(nodes) - 1, 0)
for a in results:
    print(*a)
sys.exit(1)
