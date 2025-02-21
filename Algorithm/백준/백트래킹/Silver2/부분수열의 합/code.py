n, s = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
ans = []
cnt = 0


def dfs(start):
    global cnt, ans
    if sum(ans) == s and len(ans) > 0:
        cnt += 1
    for i in range(start, n):
        ans += [arr[i]]
        dfs(i + 1)
        ans.pop()


dfs(0)
print(cnt)
