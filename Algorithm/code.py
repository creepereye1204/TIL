n = int(input())
arr = []
rst = [0] * 1002
first = True
pre_index = -1
for _ in range(n):
    l, h = map(int, input().split(" "))
    arr += [[h, l]]

arr.sort(reverse=True)
for height, index in arr:
    if first:
        pre_index = index
        first = False
        rst[index] = height
    else:
        start = min(pre_index, index)
        end = max(pre_index, index) + 1
        for i in range(start, end):
            rst[i] = max(rst[i], height)

print(sum(rst))
