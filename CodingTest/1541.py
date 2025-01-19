n = input()
m = n.split("-")
answer = sum(map(int, m[0].split("+")))
for x in m[1:]:
    answer -= sum(map(int, x.split("+")))
print(answer)
