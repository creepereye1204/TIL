n = int(input())
arr = [0] * 1002
mid_index = -1
mid_value = -1
cur = 0
rst = 0
for _ in range(n):
    l, h = map(int, input().split(" "))
    arr[l] = h
    if mid_value < h:
        mid_index = l
        mid_value = h

for i in range(mid_index + 1):
    cur = max(cur, arr[i])
    rst += cur
cur = 0
for i in range(1001, mid_index, -1):
    cur = max(cur, arr[i])
    rst += cur
print(rst)
