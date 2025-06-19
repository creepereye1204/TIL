
from collections import deque
def bfs(x,y,board):
    q=deque([[x,y]])
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    dist=[[-1]*5 for _ in range(5)]
    dist[y][x]=0
    
    while q:
        x,y=q.popleft()
        for i in range(4):
            x_=x+dx[i]
            y_=y+dy[i]
            if -1<x_<5 and -1<y_<5 and dist[y_][x_]==-1:
                if board[y_][x_]=='O':
                    dist[y_][x_]=dist[y][x]+1
                    if dist[y_][x_]<2:
                        q.append([x_,y_])
                
                elif board[y_][x_]=='P':
                    return False

    return True

def solve(place,answer):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P' and not bfs(j,i,place):
                answer.append(0)
                return
    answer.append(1)

def solution(places):
    answer = []
    for place in places:
        solve(place,answer)
                
    return answer