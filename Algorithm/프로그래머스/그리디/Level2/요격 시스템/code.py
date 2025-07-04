def solution(targets):
    answer = 0
    end=-1
    for target in sorted(targets,key=lambda x:(x[1])):
        if end<=target[0]:
            end=target[1]
            answer+=1
    return answer