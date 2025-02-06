
from collections import deque

N, M, R = map(int, input().split())

table = [list(map(str,input().split(' '))) for _ in range(N)]
answer = [[0]*M for _ in range(N)]
deq = deque()



loops=min(N,M)//2
for i in range(loops):
    deq.clear()
    deq.extend(table[i][i:M-i])
    deq.extend([row[M-i-1] for row in table[i+1:N-i-1]])
    deq.extend(table[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in table[i+1:N-i-1][::-1]])
    
    deq.rotate(-R)
    
    for j in range(i,M-i):
        answer[i][j]=deq.popleft()
    for j in range(i+1,N-i-1):
        answer[j][M-i-1]=deq.popleft()
    for j in range(M-i-1,i-1,-1):
        answer[N-i-1][j]=deq.popleft()
    for j in range(N-i-2,i,-1):
        answer[j][i]=deq.popleft()
    
    
for line in answer:
    print(" ".join(line))