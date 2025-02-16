# 일단 2차원 dp를 (n)*(n)의 2차원 배열로 만들어
# 이후 배열을 받고 투포인터를 사용하여 양옆으로 지나가며 갚이 같은지 확인해 달라지면 그때서야 양옆값을 dp에저장

n = int(input())
arr = list(map(int, input().split(" ")))
dp = [[0] * (n) for _ in range(n)]
for i in range(n):
    left = right = i
    while -1 < left and right < n and arr[left] == arr[right]:
        dp[left][right] = 1
        left -= 1
        right += 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split(" "))
    print(dp[a - 1][b - 1])
