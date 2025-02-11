# # 큐로 초기화(n) 길이로
# # 회전은 총 n-3번
# from collections import deque
# from math import prod

# rsts = []
# rst = []
# n, m = map(int, input().split(" "))
# q = deque(list(map(int, input().split(" "))))
# revers = list(map(int, input().split(" ")))


# def indexing(index):
#     global n
#     return index if index < n else index - n


# for _ in range(n):

#     rst += [prod(list(q)[:4])]
#     q.rotate(-1)

# print(rst)
# for index in revers:
#     for i in range(index, index + 4):
#         rst[indexing(i - 1)] *= -1
#     rsts += [sum(rst)]
# for rst2 in rsts:
#     print(rst2)
# 큐로 초기화(n) 길이로
# 회전은 총 n-3번


def indexing(index):
    global n
    return index if 0 <= index < n else abs(abs(index) - n)


rsts = []

n, m = map(int, input().split(" "))
q = list(map(int, input().split(" ")))
revers = list(map(int, input().split(" ")))

for i in range(n):
    rst = 1
    for j in range(4):
        rst *= q[indexing(i + j)]
    rsts += [rst]
for index in revers:
    for j in range(3, -1, -1):
        rsts[index - 1 - j] *= -1
    print(sum(rsts))
