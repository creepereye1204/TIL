text = input()
for t in ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]:
    text = text.replace(t, "*")
print(len(text))
