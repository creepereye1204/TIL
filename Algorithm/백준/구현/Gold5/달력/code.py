N = int(input())
rst = 0
calender = [0] * (365 + 2)
for _ in range(N):
    a, b = map(int, input().split(" "))
    for i in range(a, b + 1):
        calender[i] += 1
stack = []
for cal in calender:
    if cal == 0 and stack:
        rst += len(stack) * max(stack)
        stack = []
    elif cal != 0:
        stack += [cal]

print(rst)
