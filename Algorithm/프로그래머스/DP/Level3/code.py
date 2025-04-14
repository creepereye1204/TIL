
def solution(triangle):
    dp=[]
    for t in triangle:
        dp.append([-1]*len(t))
    dp[0]=triangle[0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                dp[i][j]=triangle[i][j]+dp[i-1][j]
            elif j==len(triangle[i])-1:
                dp[i][j]=triangle[i][j]+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]

    return max(dp[-1])