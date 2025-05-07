result = [0, 0]


def solution(table):
    global result
    l = len(table)
    if l == 1:
        result[table[0][0]] += 1

    else:
        temp = sum([sum(t) for t in table])
        if temp == len(table)**2:
            result[1] += 1

        elif temp == 0:
            result[0] += 1

        else:

            solution([[table[i][j] for j in range(l//2)] for i in range(l//2)])
            solution([[table[i][j] for j in range(l//2, l)]
                     for i in range(l//2)])
            solution([[table[i][j] for j in range(l//2)]
                     for i in range(l//2, l)])
            solution([[table[i][j] for j in range(l//2, l)]
                     for i in range(l//2, l)])
    return result
