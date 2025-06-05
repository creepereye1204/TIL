def solution(ingredients):
    stack = []
    answer = 0
    for ingredient in ingredients:
        stack.append(ingredient)
        if stack[-4:] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1

    return answer
