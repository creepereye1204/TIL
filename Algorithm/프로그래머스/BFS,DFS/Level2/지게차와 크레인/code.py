from collections import deque
def bfs(storage,char):
    arr=[]
    h=len(storage)
    w=len(storage[0])
    q=deque([[0,0]])
    dx=(1,0,-1,0)
    dy=(0,1,0,-1)
    visited=set((0,0))
    
    while q:
        x,y=q.popleft()
        
        for i in range(4):
            x_=x+dx[i]
            y_=y+dy[i]
            if (x_,y_) not in visited and -1<x_<w and -1<y_<h:
                if char==storage[y_][x_]:
                    arr.append((x_,y_))
                elif storage[y_][x_]==' ':
                    q.append((x_,y_))
                visited.add((x_,y_))
    
    return arr

def solve(storage,char):
    
    if len(char)==1:
        arr=bfs(storage,char)
        for x,y in arr:
            storage[y][x]=' '
        
    else:
        
        for i in range(len(storage)):
            for j in range(len(storage[0])):
                if storage[i][j]==char[0]:
                    storage[i][j]=' '
    
    
def solution(storage, requests):
    answer = 0
    
    storage=[[' ']+list(s)+[' '] for s in storage]
    storage=[[' ']*len(storage[0])]+storage+[[' ']*len(storage[0])]
    
    
    for request in requests:
        solve(storage,request)
    
    for st in storage:
        for s in st:
            if s.isalpha():
                answer+=1
    return answer