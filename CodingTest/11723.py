import sys

input = sys.stdin.readline
s = set()
n = int(input())

for _ in range(n):
    method = input().rstrip().split(" ")
    if "add" in method[0]:
        s.add(method[1])
    elif "remove" in method[0]:
        s.discard(method[1])
    elif "check" in method[0]:
        if method[1] in s:
            print(1)
        else:
            print(0)
    elif "toggle" in method[0]:
        if method[1] in s:
            s.discard(method[1])
        else:
            s.add(method[1])
    elif "all" in method[0]:
        s = set([str(i) for i in range(1, 21)])
    else:
        s = set()
