ans = 0
chkX = [False for _ in range(13)]
chkCross1 = [False for _ in range(25)]
chkCross2 = [False for _ in range(25)]


def nq(y, n):
    global ans

    if y > n:
        ans += 1
    for x in range(1, n+1):
        if chkX[x] or chkCross1[y + x] or chkCross2[(y - x) + n]:
            continue
        chkX[x] = True
        chkCross1[y + x] = True
        chkCross2[(y - x) + n] = True

        nq(y + 1, n)
        chkX[x] = False
        chkCross1[y + x] = False
        chkCross2[(y - x) + n] = False


def solution(n):
    nq(1, n)
    return ans
