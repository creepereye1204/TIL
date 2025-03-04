def solution(texts):
    stack = []
    for text in texts:
        if stack:
            if text == ")":
                stack.pop()
            else:
                stack.append(text)
        else:
            if text == ")":
                return False
            else:
                stack.append(text)

    return True if not stack else False
