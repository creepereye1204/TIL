from collections import deque

gears = [deque(list(input())) for _ in range(4)]
k = int(input())


def left(gear_idx, vector):
    if gear_idx < 0:
        return
    if gears[gear_idx + 1][6] != gears[gear_idx][2]:
        left(gear_idx - 1, -vector)
        gears[gear_idx].rotate(vector)


def right(gear_idx, vector):
    if gear_idx > 3:
        return
    if gears[gear_idx - 1][2] != gears[gear_idx][6]:
        right(gear_idx + 1, -vector)
        gears[gear_idx].rotate(vector)


for _ in range(k):
    gear_idx, vector = map(int, input().split(" "))
    gear_idx -= 1
    left(gear_idx - 1, -vector)
    right(gear_idx + 1, -vector)
    gears[gear_idx].rotate(vector)

result = 0
if gears[0][0] == "1":
    result += 1

if gears[1][0] == "1":
    result += 2

if gears[2][0] == "1":
    result += 4

if gears[3][0] == "1":
    result += 8

print(result)
