from itertools import permutations


def calc(op, num1, num2):
    if op == "*":
        return num1*num2
    elif op == "+":
        return num1+num2
    else:
        return num1-num2


def solv(op, stack):
    temp = []
    index = len(stack)
    cnt = 0
    while cnt < index:

        if stack[cnt] == op:
            temp[-1] = calc(op, temp[-1], stack[cnt+1])
            cnt += 1
        else:
            temp.append(stack[cnt])
        cnt += 1
    return temp


def solution(expression):
    answer = 0
    exp = ''.join(
        map(lambda x: ('|'+x+'|' if x in ('+', '-', '*') else x), expression)).split('|')

    exp = [int(e) if e.isdigit() else e for e in exp]
    for ops in permutations(('+', '-', '*'), 3):
        stack = exp.copy()
        for op in ops:
            stack = solv(op, stack)
        answer = max(answer, abs(stack[0]))
    return answer
