import sys

input = sys.stdin.readline


def next_permutation(text):

    k = -1
    for i in range(len(text) - 1):
        if text[i] < text[i + 1]:
            k = i
    if k == -1:
        return "".join(text)
    for i in range(len(text) - 1, -1, -1):
        if text[k] < text[i]:
            m = i
            break

    text[k], text[m] = text[m], text[k]

    return "".join(text[: k + 1] + text[k + 1 :][::-1])


T = int(input())
for _ in range(T):
    text = list(input().strip())
    print(next_permutation(text))
