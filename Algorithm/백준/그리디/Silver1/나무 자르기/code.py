n = int(input())

h = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
arr = []
rst = 0
for i in range(n):
    arr.append([a[i], h[i]])
arr.sort()
for i in range(n):
    rst = rst + arr[i][0] * i + arr[i][1]
print(rst)
