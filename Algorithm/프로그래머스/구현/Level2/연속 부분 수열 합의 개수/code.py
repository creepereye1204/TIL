

def solution(elements):
    answer = set()
    n = len(elements)
    elements.extend(elements)
    for i in range(1, n+1):

        for j in range(len(elements)-i):
            answer.add(sum(elements[j:j+i]))
    return len(answer)
