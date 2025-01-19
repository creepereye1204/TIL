n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
result = 0
for i in range(1, m - 1):
    left = max(arr[:i])
    right = max(arr[i + 1 :])
    compare = min(left, right)
    if arr[i] < compare:
        result += compare - arr[i]

print(result)
