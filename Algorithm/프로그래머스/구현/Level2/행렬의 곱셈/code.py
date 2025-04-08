def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        answer.append([])
        for a2 in list(zip(*arr2)):
            answer[-1].append(0)
            for x, y in zip(a1, a2):
                answer[-1][-1] += x*y

    return answer
