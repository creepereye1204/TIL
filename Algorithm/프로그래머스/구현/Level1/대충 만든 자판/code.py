
def solution(keymap, targets):
    answer = []
    dic={}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dic:
                dic[key[i]]=i+1
            else:
                dic[key[i]]=min(i+1,dic[key[i]])
            
    for target in targets:
        temp=0
        for t in target:
            if t in dic:
                temp+=dic[t]
            else:
                temp=-1
                break
        answer.append(temp)
    
    return answer