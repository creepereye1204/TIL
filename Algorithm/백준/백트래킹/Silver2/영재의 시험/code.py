def dfs(index, value, answer, choice, score):
    global rst
    if 5 - score <= 10 - index:
        if index == 10:

            rst += 1
            return

        for i in range(1, 6):

            if choice[0] == i:
                if choice[1] < 2:
                    if answer[index] == i:
                        dfs(index + 1, value + [i], answer, [i, choice[1] + 1], score + 1)
                    else:
                        dfs(index + 1, value + [i], answer, [i, choice[1] + 1], score)
            else:
                if answer[index] == i:
                    dfs(index + 1, value + [i], answer, [i, 1], score + 1)
                else:
                    dfs(index + 1, value + [i], answer, [i, 1], score)


rst = 0
dfs(0, [], list(map(int, input().split(" "))), [0, 0], 0)
print(rst)
