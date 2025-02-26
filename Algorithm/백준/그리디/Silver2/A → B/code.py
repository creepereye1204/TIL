a, b = map(int, input().split(" "))
rst = 1

while a <= b:

    if a == b:
        print(rst)
        exit(0)
    elif b % 10 == 1:
        b //= 10

    elif b % 2 == 0:

        b //= 2
    else:
        break
    rst += 1

print(-1)
