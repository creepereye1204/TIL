def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n]*n
    if s % n == 0:
        return answer

    cnt = s % n
    while True:
        for i in range(n):
            if cnt == 0:
                return sorted(answer)
            else:
                cnt -= 1
                answer[i] += 1
