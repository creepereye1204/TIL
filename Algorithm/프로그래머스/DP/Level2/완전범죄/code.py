def solution(info, n, m):

    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True

    for traceA, traceB in info:
        next_dp = [[False] * m for _ in range(n)]

        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue

                if a + traceA < n:
                    next_dp[a + traceA][b] = True

                if b + traceB < m:
                    next_dp[a][b + traceB] = True

        dp = next_dp

    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a

    return -1
