from collections import deque

again=True

def bfs(point,text,graph):
    global again
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    r=[]
    q=deque([[point[0],point[1]]])
    visited=[[False]*6 for _ in range(12)]
    while q:
        x,y=q.popleft()
        for i in range(4):
            x_=x+dx[i]
            y_=y+dy[i]
            if 0<=x_<6 and 0<=y_<12 and not visited[y_][x_] and graph[y_][x_]==text:
                visited[y_][x_]=True
                q+=[[x_,y_]]
                r+=[[x_,y_]]
    if len(r)>3:
        for r_ in r:
            graph[r_[1]][r_[0]]='.'
        again=True

def simulation(graph):
    new_graph=[['.']*6 for _ in range(12)]
    
    for idx,col in enumerate(list(zip(*graph))):
        
        index=11
        for i in range(11,-1,-1):
            if col[i]!='.':
                new_graph[index][idx]=col[i]
                index-=1
    return new_graph

def solution(graph):
    global again
    
    cnt=-1
    while again:
        again=False
        cnt+=1
        for i in range(12):
            for j in range(6):
                text=graph[i][j]
                if text!='.':
                    bfs((j,i),text,graph)
        
        graph=simulation(graph)
        
    
    return cnt

graph=[list(input()) for _ in range(12)]
print(solution(graph))