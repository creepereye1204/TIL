n = int(input())
texts = [input() for _ in range(n)]
texts.sort(key=len)
rst = 0
for i in range(n):
    for j in range(i + 1, n):
        if texts[i] == texts[j][: len(texts[i])]:
            rst += 1
            break
print(n - rst)
