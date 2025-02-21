# stack = []
# for _ in range(int(input())):
#     arr = input().split(" ")
#     if arr[0] == "push":
#         stack += [int(arr[1])]

#     elif arr[0] == "top":
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)
#     elif arr[0] == "pop":
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
#     elif arr[0] == "size":
#         print(len(stack))
#     else:
#         if stack:
#             print(0)
#         else:
#             print(1)
# 스택이 있는지부터 확인
# 있으면 마지막 값과 arr의값을 비교
# 마지막 값이 작으면 queue에서 푸시
# 크면 pop (종료 NO)
# 같은면 스택이랑 arr 팝
from collections import deque

n = int(input())
arr = deque([])
stack = []
rst = []
queue = deque([])
for i in range(1, n + 1):
    queue += [i]
    arr += [int(input())]

while queue or arr:
    if not stack:
        stack += [queue.popleft()]
        rst += ["+"]
    else:
        if stack[-1] == arr[0]:
            stack.pop()
            arr.popleft()
            rst += ["-"]
        elif stack[-1] < arr[0]:
            stack += [queue.popleft()]
            rst += ["+"]
        else:
            print("NO")
            exit(0)

for r in rst:
    print(r)
