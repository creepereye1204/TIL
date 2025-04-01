def solution(arr):
    from math import gcd
    answer = arr[0]

    for a in arr:
        answer = answer*a//gcd(answer, a)

    return answer
