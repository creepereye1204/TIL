from itertools import combinations

rst = 1000000000
n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

houses = []
chikens = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chikens += [(j, i)]
        elif graph[i][j] == 1:
            houses += [(j, i)]

for spots in list(combinations(chikens, m)):
    cnt = 0
    for house in houses:
        l = 1000000000
        for spot in spots:
            l = min(l, abs(house[0] - spot[0]) + abs(house[1] - spot[1]))
        cnt += l
    rst = min(rst, cnt)


print(rst)
