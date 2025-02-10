N = int(input())
M = int(input())
target = input()

find = "IO" * (N) + "I"
cnt = 0
for i in range(M):
    t = target[i:]
    if t.startswith(find):
        cnt += 1

print(cnt)
