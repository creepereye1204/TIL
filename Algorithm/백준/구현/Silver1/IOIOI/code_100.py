N = int(input())
M = int(input())
target = input()

ans, i, count = 0, 0, 0

while i < M - 2:
    if target[i : i + 3] == "IOI":
        count += 1
        i += 2
        if count == N:
            ans += 1
            count -= 1
    else:
        count = 0
        i += 1
print(ans)
