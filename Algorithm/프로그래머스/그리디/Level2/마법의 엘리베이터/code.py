def solution(storey):
    answer = 0
    while storey:
        temp = storey % 10
        if temp < 5:
            answer += temp
        elif temp > 5:
            answer += 10-temp
            storey += 10
        else:
            if (storey//10) % 10 > 4:
                storey += 10
            answer += temp
        storey //= 10
    return answer
