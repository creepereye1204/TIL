def solution(n):
    answer = [1]*(n+1)
    for i in range(2, n+1):
        answer[i] = (answer[i-2]+answer[i-1]) % 1234567
    return answer[-1]
