from math import gcd


def solution(arrayA, arrayB):
    gcdA = nGCD(arrayA)
    gcdB = nGCD(arrayB)

    a1 = gcdA if condition(gcdA, arrayB) else 0
    a2 = gcdB if condition(gcdB, arrayA) else 0
    return max(a1, a2)


def nGCD(array):
    result = array[0]
    for i in range(1, len(array)):
        result = gcd(result, array[i])
    return result


def condition(n, array):
    if n == 1:
        return False
    for a in array:
        if a % n == 0:
            return False
    return True
