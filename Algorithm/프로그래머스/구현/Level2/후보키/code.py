from itertools import combinations


def solve(combo, relation, height):
    rst = set()
    for i in range(height):
        row = ''
        for j in combo:
            row = row+relation[i][j]
        if row in rst:
            return False
        else:
            rst.add(row)

    return True


def solution(relation):

    width = len(relation[0])
    height = len(relation)
    nums = list(range(width))

    answer = 0
    combos = []

    for i in range(1, width+1):
        for combo in combinations(nums, i):
            if solve(combo, relation, height):
                combos.append(combo)

    while combos:
        c = combos.pop()
        check = True
        for combo in combos:

            if len(set(c) | set(combo)) == max(len(c), len(combo)):
                check = False
                break

        if check:
            answer += 1
    return answer
