import heapq

n, m = map(int, input().split(" "))
temps = list(map(int, input().split(" ")))
students = list(map(int, input().split(" ")))
presents = []
for temp in temps:
    heapq.heappush(presents, -temp)

for student in students:
    present = -heapq.heappop(presents)
    if student > present:
        print(0)
        exit(0)
    else:
        heapq.heappush(presents, -(present - student))
print(1)
