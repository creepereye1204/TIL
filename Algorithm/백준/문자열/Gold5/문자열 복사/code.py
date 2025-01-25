S = input()
P = input()
index = 0
rst = 1
for i in range(1, len(P)):
    if S.find(P[index : i + 1]) == -1:
        index = i
        rst += 1
print(rst)
