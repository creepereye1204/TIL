def solution(s, skip, index):
    answer = ''
    temp = set(list(s))
    skip = set(list(skip))
    dic = {}
    for t in temp:
        cnt = 0
        c = t
        while cnt < index:
            c = ord(c)+1
            if c > ord('z'):
                c = ord('a')
            c = chr(c)
            if c not in skip:
                cnt += 1

        dic[t] = c
    for a in s:
        answer = answer+dic[a]
    return answer
