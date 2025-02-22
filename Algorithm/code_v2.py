import sys

sys.setrecursionlimit(10**9)


def check(value, i):
    global l, texts, visited, candidates
    if not value:
        return True
    if not visited[i] and value[-1] != texts[i] and value + texts[i] not in candidates:
        return True
    return False


texts = input()
l = len(texts)
candidates = set()
rst = set()
visited = [False] * l


def dfs(cnt, value):
    global l, candidates, texts, visited, rst
    if value:
        candidates.add(value)
    if cnt == l:
        rst.add(value)
        return
    for i in range(l):
        if check(value, i):
            visited[i] = True
            dfs(cnt + 1, value + texts[i])
            visited[i] = False


dfs(0, "")
print(len(rst))
