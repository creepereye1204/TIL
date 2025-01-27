from collections import deque,defaultdict
rst=0
tree=defaultdict(lambda :-1)
def bfs(i,graph):
    cnt=0
    q=deque([i])
    visisted=[i]
    dist=[0]*501
    while q:
        v=q.popleft()
        print(v)
        for node in graph[v]:
            if node not in visisted:
                visisted+=[node]
                dist[node]=dist[v]+1
                q+=[node]
                cnt+=1
    return cnt,max(dist)

n,m = map(int,input().split(' '))
graph=[[] for _ in range(501)]
for _ in range(m):
    a,b = map(int,input().split(' '))
    graph[b]+=[a]
    
for i in range(1,n+1):
    cnt,depth=bfs(i,graph)
    
    if tree[depth]==-1:
        tree[depth]=cnt
    elif tree[depth]!=-1:
        tree[depth]=-2

for key,value in tree.items():
    cnt=0
    if value>0:
        for key_ in tree.keys():
            if key_<key:
                cnt+=1
        if value==cnt:
            rst+=1
print(rst)
print(tree)     
        
        
    