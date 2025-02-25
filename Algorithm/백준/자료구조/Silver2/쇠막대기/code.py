text = input().replace("()", "|")
stack = 0
rst = 0
for t in text:
    if t == "(":
        stack += 1
    elif t == "|":
        rst += stack
    else:
        rst += 1
        stack -= 1
print(rst)
