from collections import deque

trucks_count, bribge_length, limit_weight = map(int, input().split(" "))
trucks = deque(map(int, input().split(" ")))
bribge = deque([0] * bribge_length)
time = 0

while trucks:
    truck = bribge.popleft()
    limit_weight += truck
    if 0 <= limit_weight - trucks[0]:

        truck = trucks.popleft()
        limit_weight -= truck

        bribge += [truck]

    else:
        bribge += [0]
    time += 1
print(time + bribge_length)
