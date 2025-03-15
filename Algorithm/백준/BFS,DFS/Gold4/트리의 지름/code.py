import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(parent,now):
    global visited,tree
    for child,dist in tree[parent]:
        if visited[child]==-1:
            visited[child]=now+dist
            dfs(child,visited[child])

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    parent,child,dist=map(int,input().split(' '))
    tree[parent].append((child,dist))
    tree[child].append((parent,dist))
    
visited=[-1]*(n+1)
visited[1]=0
dfs(1,0)
start_node=visited.index(max(visited))
visited=[-1]*(n+1)
visited[start_node]=0
dfs(start_node,0)
print(max(visited))