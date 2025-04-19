
def solution(msg):
    answer = []
    dict = {chr(t):i+1 for i,t in enumerate(range(ord('A'),ord('Z')+1))}

    while msg:
        if msg in dict.keys():
            return answer+[dict[msg]]
        for i in range(1,len(msg)+1):
            if msg[:i] not in dict.keys():
                break
        dict[msg[:i]]=len(dict.keys())+1
        answer.append(dict[msg[:i-1]])
        msg=msg[i-1:]

    return answer