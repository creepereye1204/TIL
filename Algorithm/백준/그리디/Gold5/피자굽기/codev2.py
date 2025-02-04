d, n = map(int, input().split())
data = list(map(int, input().split()))
pizza = list(map(int, input().split()))
oven = [data[0]]
for i in range(1, len(data)):
    oven += [min(data[i], oven[i - 1])]


cnt = 0
i = d - 1

while i >= 0:
    if oven[i] >= pizza[cnt]:
        cnt += 1
        if cnt == n:
            break
    i -= 1

print(i + 1 if cnt == n else 0)
