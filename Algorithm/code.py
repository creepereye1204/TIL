from collections import deque

def bfs(dist,x,y,graph):
    q=deque([[x,0]])
    visited=set([x])
    
    while q:
        node,dis=q.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                q.append([i,dis+dist[node][i]])
                if i==y:
                    return q[-1][1]
                
def solution(dist,graph,qs):
    for x,y in qs:
        print(bfs(dist,x,y,graph))
    

n,m=map(int,input().split(' '))
dist=[[-1]*(n+1) for _ in range(n+1)]
graph=[[] for _ in range(n+1)]
qs=[]
for _ in range(n-1):
    a,b,c=map(int,input().split(' '))
    dist[a][b]=c
    dist[b][a]=c
    graph[a].append(b)
    graph[b].append(a)

for _ in range(m):
    a,b=map(int,input().split(' '))
    qs.append([a,b])

solution(dist,graph,qs)