rst = 0
for _ in range(int(input())):

    word = input()
    text = set()
    flage = ""
    for w in word:
        if w not in text:
            text.add(w)
            flage = w
        elif w in text and w != flage:
            break
    else:
        rst += 1

print(rst)
