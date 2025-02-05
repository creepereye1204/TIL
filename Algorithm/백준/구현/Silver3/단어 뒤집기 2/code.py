arr = input().replace(" ", "|").replace("<", " <").replace(">", "> ").split(" ")

for a in arr:
    if a:
        if a[0] == "<":
            print(a.replace("|", " "), end="")
        else:
            temp = []
            for b in a.split("|"):
                temp.append(b[::-1])
            print(" ".join(temp), end="")
