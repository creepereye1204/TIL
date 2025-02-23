import sys

sys.setrecursionlimit(10**9)


def check(value, i):
    global texts, visited
    if not value:
        return True
    if not visited[i] and value[-1] != texts[i]:
        return True
    return False


texts = input()
l = len(texts)
candidates = set()
rst = 0
visited = [False] * l


def dfs(cnt, value):
    global l, candidates, texts, visited, rst
    if cnt == l:
        rst += 1
        return
    for i in range(l):
        if check(value, i):
            visited[i] = True
            dfs(cnt + 1, texts[i])
            visited[i] = False


dfs(0, "")
print(rst)
