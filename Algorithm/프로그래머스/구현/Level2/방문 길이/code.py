from collections import deque
def solution(q):
    q=deque(q)
    answer=set()
    dirs={'L':(-1,0),'R':(1,0),'U':(0,-1),'D':(0,1)}
    x=y=0
    while q:
        dir=q.popleft()
        x_,y_=dirs[dir]
        if -5<=x+x_<=5 and -5<=y+y_<=5:
            max_x=max(x,x+x_)
            max_y=max(y,y+y_)
            min_x=min(x,x+x_)
            min_y=min(y,y+y_)
            answer.add((min_x,max_x,min_y,max_y))
            x+=x_
            y+=y_
    return len(answer)
