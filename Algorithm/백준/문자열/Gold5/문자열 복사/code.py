S = input()
P = input()
rst = 0

while P:
    index = 0
    mx_l = -1
    flag = False
    cnt = 0
    for i in range(min(len(S), len(P))):

        if P[index] == S[i]:
            index += 1
            cnt += 1
            flage = True
            mx_l = max(cnt, mx_l)

        elif flag:
            index = 0
            cnt = 0
            flage = False

    P = P[mx_l:]
    rst += 1

print(rst)
