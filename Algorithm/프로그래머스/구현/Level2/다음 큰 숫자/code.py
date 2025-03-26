def solution(n):
    cnt = (bin(n)[2:]).count('1')
    n += 1
    while cnt != (bin(n)[2:]).count('1'):
        n = int(bin(n)[2:], 2)+1

    return n
