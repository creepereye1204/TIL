def solution(citations):
    citations.sort()
    answer = 0
    for i in range(1,max(citations)+1):
        cnt=0
        for citation in citations:
            if citation<i:
                cnt+=1
        if cnt <= i and i<= len(citations)-cnt:
            answer=i
    
    
    return answer