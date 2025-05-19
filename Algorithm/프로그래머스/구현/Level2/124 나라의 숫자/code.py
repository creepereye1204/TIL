def solution(n):
    answer=''
    while n:
        n,mod=divmod(n-1,3)
        answer='124'[mod]+answer
    return answer
        