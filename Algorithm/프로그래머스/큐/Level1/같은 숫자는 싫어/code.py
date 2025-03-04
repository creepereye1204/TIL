def solution(arr):
    answer = []
    temp = -1
    for a in arr:
        if a != temp:
            answer.append(a)
            temp = a

    return answer
