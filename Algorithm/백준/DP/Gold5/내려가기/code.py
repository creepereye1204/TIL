import sys

def solution():
    input=sys.stdin.readline
    n=int(input())
    INF=sys.maxsize
    dx=[-1,0,1]
    dp1=[-INF]*3
    dp2=[INF]*3

    for i in range(n):
        if i==0:
            p=list(map(int,input().split(' ')))
            dp1=p.copy()
            dp2=p.copy()
        else:
            p=list(map(int,input().split(' ')))
            
            mn=[INF]*3
            mx=[-INF]*3
            
            for j in range(3):
                
                for x in dx:
                    if 0<=j+x<3:
                        mx[j]=max(mx[j],dp1[j+x]+p[j])
                        mn[j]=min(mn[j],dp2[j+x]+p[j])
  
            dp1=mx
            dp2=mn
        
    print(max(dp1),min(dp2))
    
solution()