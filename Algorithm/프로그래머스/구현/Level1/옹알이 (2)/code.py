def solution(babblings):
    answer = 0
    tt=["aya", "ye", "woo", "ma"]
    for babbling in babblings:
        for index,t in enumerate(tt):
            babbling=babbling.replace(t,str(index+1))
        if not babbling.isdigit():
            continue
        temp=''
        for b in babbling:
            if temp!=b:
                temp=b
            else:
                break
        else:
            answer+=1
    return answer