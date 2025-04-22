def solution(lands):
    dp = [[0]*4 for _ in range(len(lands))]
    dp[0] = lands[0]
    for i in range(1, len(lands)):
        for j in range(4):
            mx = 0
            for k in range(4):
                if j != k:
                    mx = max(dp[i-1][k], mx)
            dp[i][j] = mx+lands[i][j]

    return max(dp[-1])
