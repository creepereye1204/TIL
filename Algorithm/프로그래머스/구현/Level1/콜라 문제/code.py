def solution(a, b, n):
    answer = 0
    while a <= n:
        div, mod = divmod(n, a)
        answer += div*b
        n = mod+div*b
    return answer
