def solution(n, m, section):
    answer = index = 0
    m -= 1
    for s in section:
        if index < s:
            index = s+m
            answer += 1

    return answer
