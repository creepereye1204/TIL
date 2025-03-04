def solution(number, k):
    answer = []  # Stack

    for num in number:
        while answer and k > 0 and num > answer[-1]:
            k -= 1
            answer.pop()
        answer.append(num)
    return "".join(answer)[: len(number) - k]
