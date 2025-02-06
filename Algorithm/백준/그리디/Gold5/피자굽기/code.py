d, n = map(int, input().split(" "))
oven = list(map(int, input().split(" ")))
bread = list(map(int, input().split(" ")))

depth = d
for b in bread:

    for i in range(depth):
        if oven[i] >= b:

            depth = i
        else:
            if i == 0:

                print(0)
                exit()
            break
print(depth + 1)
