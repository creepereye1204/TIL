import sys


word = list(map(str, sys.stdin.readline().strip()))
temp = {"H": 1, "C": 12, "O": 16}
stack = []

# 반복문을 통해 문자를 확인
for i in word:

    if i == "(":
        stack.append(i)

    elif i == ")":
        check = 0

        # 반복문을 통해 괄호 안에 있는 수를 더하여 stack에 추가
        while stack[-1] != "(":
            target = stack.pop()

            check += target
        stack.pop()
        stack.append(check)

    # 문자가 원자라면 stack에 원자량을 추가
    elif i.isalpha():
        stack.append(temp[i])

    # 입력받은 문자가 괄호도 아니고 원자도 아니면 숫자이므로
    # stack에 마지막 숫자를 입력받은 문자로 곱해준다.
    else:
        stack[-1] *= int(i)

print(sum(stack))
