n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
for i in range(n - 2):
    if arr[i] < arr[i + 1] + arr[i + 2]:
        print(sum(arr[i : i + 3]))
        exit()
print(-1)
