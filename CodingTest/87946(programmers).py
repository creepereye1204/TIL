from itertools import permutations

def solution(k, dungeons):
    
    answer = -1
    for value in list(permutations(dungeons,len(dungeons))):
        cnt=0
        money=k
        for v in value:
            at_least,cost=v[0],v[1]
            if money>=at_least:
                money-=cost
                cnt+=1
            else:
                break
        answer=max(answer,cnt)
    
    return answer