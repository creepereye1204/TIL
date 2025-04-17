def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for index in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[index]:
            answer[stack.pop()]=numbers[index]
        stack.append(index)
    return answer