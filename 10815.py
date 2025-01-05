import sys

input = sys.stdin.readline
N = int(input())
cards = {n: "" for n in list(map(int, input().split(" ")))}
M = int(input())
numbers = list(map(int, input().split(" ")))
for n in numbers:
    try:
        cards[n]
        print(1, end=" ")
    except KeyError:
        print(0, end=" ")
