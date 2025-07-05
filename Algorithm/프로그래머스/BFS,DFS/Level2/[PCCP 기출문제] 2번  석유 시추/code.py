
def solution(land):
    dic = {}
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    answer = 0
    id = 2
    h = len(land)
    w = len(land[0])
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                cnt = 1
                q = [(j, i)]
                land[i][j] = id
                while q:
                    x, y = q.pop()
                    for k in range(4):
                        x_ = dx[k]+x
                        y_ = dy[k]+y
                        if 0 <= y_ < h and 0 <= x_ < w and land[y_][x_] == 1:
                            land[y_][x_] = id
                            cnt += 1
                            q.append((x_, y_))

                dic[id] = cnt
                id += 1

    return max([sum([dic[g] if g > 1 else 0 for g in set(l)]) for l in zip(*land)])
