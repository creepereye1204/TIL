# 이후 모든 좌표에서 오른쪽 아래 가로를 확인한다.
#


def check(target):
    global graph

    dx = [1, 1, 0, -1]
    dy = [0, 1, 1, 1]
    rst = 0
    for y in range(5):
        for x in range(5):

            for i in range(4):
                flage = False
                for cnt in range(5):
                    x_ = x + cnt * dx[i]
                    y_ = y + cnt * dy[i]
                    if 0 <= x_ < 5 and 0 <= y_ < 5 and graph[y_][x_]:
                        pass
                    else:
                        flage = True
                        break

                if not flage:
                    rst += 1
                    if rst == 3:
                        print(target)
                        exit(0)

                        return


# 딕셔너리에 번호별로 좌표를 저장한다
# 순서대로 번호표를 뽑으면서 해당좌표를 True로 만든다.

table = [list(map(int, input().split(" "))) for _ in range(5)]
graph = [[False] * 5 for _ in range(5)]
dic = {}
arr = []
for i in range(5):
    for j in range(5):
        dic[table[i][j]] = [j, i]
for _ in range(5):
    arr += [list(map(int, input().split(" ")))]
cntc = 0
for a in arr:
    for b in a:
        cntc += 1
        x, y = dic[b]
        graph[y][x] = True
        check(cntc)
