n = int(input())
ground = [int(input()) for _ in range(n)]
prior = sorted([[g, idx] for idx, g in enumerate(ground)], key=lambda x: (-x[0], x[1]))

plate = [False] * n
rst = []


def press(index):
    global n, ground, plate, rst

    rst += [index + 1]
    left = right = index
    plate[index] = True
    l_flage = r_flage = True
    while l_flage or r_flage:
        left -= 1
        right += 1
        if 0 <= left and ground[left + 1] > ground[left] and not plate[left]:
            plate[left] = True
        else:
            l_flage = False

        if right < n and ground[right - 1] > ground[right] and not plate[right]:
            plate[right] = True
        else:
            r_flage = False

    if all(plate):
        for r in sorted(rst):
            print(r)
        exit(0)


for p in prior:
    if not plate[p[1]]:
        press(p[1])
