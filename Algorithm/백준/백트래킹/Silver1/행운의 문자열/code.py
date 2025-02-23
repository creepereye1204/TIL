import sys
from collections import Counter

rst = 0


def backtrack(num, pre_word):
    global cnt, words, rst, n
    if len(n) == num:
        rst += 1
        return
    for key in words.keys():
        if words[key] != 0 and pre_word != key:
            words[key] -= 1
            backtrack(num + 1, key)
            words[key] += 1


n = input()
words = Counter(n)

cnt = Counter(words)
backtrack(0, "")
print(rst)
