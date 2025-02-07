t = input()
mx_text = t.replace("K", "K|").split("|")
mn_text = t.replace("K", "|K|").split("|")

mx = mn = ""
for text in mx_text:
    if text:
        if text[-1] == "K":
            mx = mx + str(5 * 10 ** (len(text) - 1))
        else:
            mx = mx + "1" * len(text)
print(mx)
for text in mn_text:
    if text:
        if text == "K":
            mn = mn + "5"
        else:
            mn = mn + str(10 ** (len(text) - 1))
print(mn)
