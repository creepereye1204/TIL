from collections import Counter


def solution(weights):
    counter = Counter(weights)
    answer = 0
    for k, v in counter.items():
        if v > 1:
            answer += v*(v-1)/2
    weights = set(weights)

    for weight in weights:
        if weight*2/3 in weights:
            answer += counter[weight*2/3]*counter[weight]
        if weight*3/4 in weights:
            answer += counter[weight*3/4]*counter[weight]
        if weight*2/4 in weights:
            answer += counter[weight*2/4]*counter[weight]
    return answer
