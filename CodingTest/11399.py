a, b, _ = 0, 0, input()
for i in sorted(list(map(int, input().split(" ")))):
    a += i
    b += a
print(b)
