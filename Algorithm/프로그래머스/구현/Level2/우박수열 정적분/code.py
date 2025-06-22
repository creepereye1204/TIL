from itertools import accumulate


def solution(k, ranges):
    arr = [k]
    while k > 1:
        if k % 2 == 0:
            k /= 2

        else:
            k = k*3+1
        arr.append(k)

    arr = [(arr[i]+arr[i+1])/2 for i in range(len(arr)-1)]
    arr = [0]+list(accumulate(arr))
    l = len(arr)-1
    answer = []
    for a, b in ranges:
        b = l+b

        if a < b:
            answer.append(arr[b]-arr[a])
        elif a == b:
            answer.append(0.0)
        else:
            answer.append(-1)

    return answer
