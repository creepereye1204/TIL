# import heapq

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))


# result = []


# q = [[a] for a in arr]


# heapq.heapify(q)

# while q:
#     v = heapq.heappop(q)
#     for a in arr:
#         if len(v) == M:
#             heapq.heappush(result, v)
#             break

#         if v[-1] <= a:
#             new_v = v + [a]
#             heapq.heappush(q, new_v)


# for r in result:
#     print(" ".join(map(str, r)))
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def DFS(lst):
    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return
    for a in arr:
        if len(lst) == 0:
            DFS([a])
        else:
            if lst[-1] <= a:
                DFS(lst + [a])


DFS([])
