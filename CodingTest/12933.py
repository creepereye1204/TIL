s = input()
visited = [False] * len(s)
cnt = 0
quack = "quack"

if len(s) % 5 != 0:
    print(-1)
    exit()


def sol():
    global cnt
    idx = 0
    new = True
    for i in range(len(s)):
        if quack[idx] == s[i] and not visited[i]:
            visited[i] = True
            if quack[idx] == "k":
                if new:
                    cnt += 1
                    new = False
                idx = 0
            else:
                idx += 1


for _ in range(len(s)):
    sol()
if not all(visited) or cnt == 0:
    cnt = -1
print(cnt)
