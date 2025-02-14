# 일단 디폴트 디셔너리로 dp만들기단 처음에 0으로 초기화
# 이후 문자열을 입력받고 0으로 초기화
# 이루 점화식 대로 하고 문자 하나 빼기는 for 문으로 따로 for문 2개

from collections import defaultdict, deque

dp = defaultdict(int)
s = input()
m = int(input())
arr = []
for _ in range(m):
    a, x = map(str, input().split(" "))
    x = int(x)
    arr += [[a, x]]


q = deque([s])

while q:
    v = q.popleft()

    for text, cost in arr:
        if text in v:
            node = v.replace(text, "", 1)
            if dp[node] < dp[v] + cost:
                dp[node] = dp[v] + cost
                if node != "":
                    q += [node]

    for i in v:
        if i in v:
            node = v.replace(i, "", 1)
            if dp[node] < dp[v] + 1:
                dp[node] = dp[v] + 1
                if node != "":
                    q += [node]

print(dp[""])
