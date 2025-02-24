text = input().split("-")
rst = 0
rst += sum(list(map(int, text[0].split("+"))))
for t in range(1, len(text)):
    rst -= sum(list(map(int, text[t].split("+"))))
print(rst)
