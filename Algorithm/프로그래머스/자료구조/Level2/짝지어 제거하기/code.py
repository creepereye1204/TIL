def solution(ss):
    stack=[]
    for s in ss:
        if stack:
            if stack[-1]!=s:
                stack.append(s)
            else:
                stack.pop()
        else:
            stack.append(s)

    return 1 if not stack else 0