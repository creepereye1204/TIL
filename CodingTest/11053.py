# DP
# n = int(input())
# arr = list(map(int, input().split(" ")))
# dp = [1] * n
# for i in range(1, n):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# BS
n = int(input())
arr = list(map(int, input().split()))
rst = [arr[0]]


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left


for i in range(1, n):
    if rst[-1] < arr[i]:
        rst += [arr[i]]
    else:
        index = binary_search(rst, arr[i])
        rst[index] = arr[i]
print(len(rst))
