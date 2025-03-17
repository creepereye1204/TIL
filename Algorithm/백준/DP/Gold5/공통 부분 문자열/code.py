A=input()
B=input()
rst=0
dp=[[0]*(len(A)) for _ in range(len(B))]
for i in range(len(B)):
    for j in range(len(A)):
        if A[j]==B[i]:
            if i==0 or j==0:
                dp[i][j]=1
            else:

                dp[i][j]=dp[i-1][j-1]+1
            rst=max(rst,dp[i][j])
print(rst)