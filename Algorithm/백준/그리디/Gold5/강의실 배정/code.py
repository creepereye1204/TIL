import heapq

heaps = []
times = []
n = int(input())
for i in range(n):
    a, b = map(int, input().split(" "))
    times.append((a, b))

times.sort(key=lambda x: (x[0], x[1]))
heaps += [times.pop(0)[1]]
for time in times:
    if heaps[0] <= time[0]:
        heapq.heappop(heaps)

    heapq.heappush(heaps, time[1])
print(len(heaps))
