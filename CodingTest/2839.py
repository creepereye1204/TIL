def solution(N):
    dp = [5001] * (5000 + 1)
    dp[3] = 1
    dp[5] = 1
    dp[6] = 2
    for i in range(6, N + 1):

        dp[i] = min(dp[i - 5], dp[i - 3]) + 1

    return dp[N] if 5000 > dp[N] else -1


print(solution(int(input())))
