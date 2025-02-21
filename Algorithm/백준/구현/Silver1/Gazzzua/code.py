money = 0


def divide(stoks):
    global money
    if len(stoks) < 2:
        return
    mx = max(stoks)
    index = stoks.index(mx)

    for stock in stoks[:index]:
        money = money - stock + stoks[index]
    divide(stoks[index + 1 :])


input()
divide(list(map(int, input().split(" "))))
print(money)
