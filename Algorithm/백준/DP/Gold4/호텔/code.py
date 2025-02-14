import sys

INF = sys.maxsize
n, c = map(int, input().split(" "))
dp = [INF] * (n + 1)
dp[0] = 0
costs, clients = [0], [0]
for _ in range(c):
    cost, client = map(int, input().split(" "))
    costs += [cost]
    clients += [client]


for index in range(1, n + 1):

    for j in range(1, c + 1):

        if index - clients[j] < 1:
            dp[index] = min(dp[index], costs[j])

        else:
            dp[index] = min(dp[index], dp[index - clients[j]] + costs[j])

print(dp[n])
