from collections import deque
def bfs(home_x,home_y,festival_x,festival_y,nodes,visited):
    q=deque([[home_x,home_y]])
    while q:
        x,y=q.popleft()
        if abs(festival_x-x)+abs(festival_y-y)<=1000:
            return 'happy'
        for node in nodes:
            if abs(node[0]-x)+abs(node[1]-y)<=1000 and node not in visited:
                visited.add(node)
                q.append(node)
    return 'sad'

for _ in range(int(input())):
    n=int(input())
    home_x,home_y=map(int,input().split(' '))
    nodes=[]
    for _ in range(n):
        x,y=map(int,input().split(' '))
        nodes.append((x,y))
    festival_x,festival_y=map(int,input().split(' '))
    print(bfs(home_x,home_y,festival_x,festival_y,nodes,set()))