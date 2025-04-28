def solution(n):
    a = b = 0
    for i in range(n):
        if i == 0:
            a = b = 1
        elif i == 1:
            b = 2
        else:
            temp = b
            b = (a+b) % 1000000007
            a = temp
    return b
