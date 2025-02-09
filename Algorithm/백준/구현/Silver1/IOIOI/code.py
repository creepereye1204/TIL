n = int(input())
m = int(input())
text = input().replace("IO", "K")

results = []
cnt = 0
for t in text:
    if t == "K":
        cnt += 1
    else:
        if cnt != 0:
            if t == "I":
                results += [cnt]
            else:
                cnt -= 1
                results += [cnt]
        cnt = 0
if cnt != 0:
    results += [cnt - 1]

rst = 0
for result in results:
    if result != 0:
        rst += result - n + 1
print(rst)
