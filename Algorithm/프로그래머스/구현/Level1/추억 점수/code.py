def solution(name, yearning, photos):
    dic=dict(zip(name, yearning))
    answer = []
    for photo in photos:
        temp=0
        for p in photo:
            if p in dic:
                temp+=dic[p]
        answer.append(temp)
    return answer