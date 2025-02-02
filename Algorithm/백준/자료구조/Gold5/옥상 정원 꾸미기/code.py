n = int(input())
height = [int(input()) for _ in range(n)]

stack = []
cnt = 0

for cur in height:
    while stack and stack[-1] <= cur:
        stack.pop()  # 옥상을 볼 수 없는 관리인은 전부 제거

    cnt += len(stack)  # 옥상을 볼 수 있는 관리인 수
    stack.append(cur)  # 현 빌딩을 스택에 추가

print(cnt)
