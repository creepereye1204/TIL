N, M = map(int, input().split())
trains = [[False] * 20 for _ in range(N)]
for _ in range(M):
    v = list(map(int, input().split()))
    if v[0] == 1:
        trains[v[1] - 1][v[2] - 1] = True
    elif v[0] == 2:
        trains[v[1] - 1][v[2] - 1] = False
    elif v[0] == 3:
        trains[v[1] - 1] = [False] + trains[v[1] - 1][:-1]
    else:
        trains[v[1] - 1] = trains[v[1] - 1][1:] + [False]

res = []
for train in trains:
    if train not in res:
        res.append(train)
print(len(res))
