def solution(n, left, right):
    
    answer = []
    a=left//n
    b=left%n
    c=right//n
    d=right%n
    for i in range(a,c+1):
        for j in range(1,n+1):
            answer.append(max(i+1,j))
    
    if -(n-d)==-1:
        return answer[b:]
    return answer[b:-(n-d)+1]