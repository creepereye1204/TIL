input()
arr = list(map(int, input().split(" ")))
temp = set(arr.copy())
temp = sorted(list(temp))
dic = {}
for i in range(len(temp)):
    dic[temp[i]] = i
for a in arr:
    print(dic[a], end=" ")
