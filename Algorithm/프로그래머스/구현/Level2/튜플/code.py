def solution(s):
    answer = []
    s=s[2:-2].split('},{')
    s=list(map(lambda x: x.split(','),s))
    s.sort(key=len)
    for i in s:

        for j in i:

            if j not in answer:
                answer.append(j)
                break
    return list(map(int,answer))