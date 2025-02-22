from itertools import permutations


def check(value, l):
    for i in range(1, l + 1):

        if value[i - 1] == value[i] or value[i] == value[i + 1]:
            return 0
    return 1


rst = 0
text = input()
l = len(text)
for value in set(permutations(text, l)):
    rst += check([" "] + list(value) + [" "], l)

print(rst)
