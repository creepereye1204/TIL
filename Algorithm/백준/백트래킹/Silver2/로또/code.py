import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(index, arr):
    global k, visited, text

    if len(arr) == 6:
        print(*arr)
        return
    for i in range(index, k):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, arr + [text[i]])
            visited[i] = False


while True:
    text = list(map(int, input().split(" ")))

    if text[0] == 0:
        break
    text = text[1:]
    visited = [False] * len(text)
    k = len(text)

    dfs(0, [])
    print()
