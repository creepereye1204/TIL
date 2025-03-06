p, limit = map(int, input().split(" "))
rooms = []
for idx in range(p):
    score, player = map(str, input().split(" "))
    for room in rooms:
        if room[0][0] - 10 <= int(score) <= room[0][0] + 10 and len(room) < limit:
            room.append([int(score), player])
            break
    else:
        rooms.append([[int(score), player]])
for room in rooms:
    if len(room) == limit:
        print("Started!")
    else:
        print("Waiting!")
    for info in sorted(room, key=lambda x: (x[1], x[0])):
        print(*info)
