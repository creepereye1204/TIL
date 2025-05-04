def solution(routes):
    answer = 0
    flage = -1000000
    for start, end in sorted(routes, key=lambda x: (x[1], x[0])):
        if flage < start:
            answer += 1
            flage = end
    return answer
