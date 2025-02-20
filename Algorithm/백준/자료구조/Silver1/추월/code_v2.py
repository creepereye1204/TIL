n = int(input())
cars = {}
outs = []
cnt = 0
for index in range(n):
    cars[input()] = index

for _ in range(n):
    outs += [cars[input()]]

for i in range(n):
    now = outs[i]
    for j in range(i + 1, n):
        if now > outs[j]:
            cnt += 1
            break
print(cnt)
