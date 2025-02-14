```python


for index in range(1, n + 1): # <-이 부분 1씩 증가하기 때문에 dp[n]이 INF 일 걱정은 없음

    for j in range(1, c + 1):

        if index - clients[j] < 1:
            dp[index] = min(dp[index], costs[j]) # <- 이 부분이 핵심!!!!!!!! 이걸 물어본 거나 마찬가지! 최소한이라고 했으므로 index 일 때 그 이상의 client를 먹어도 상관없음!

        else:
            dp[index] = min(dp[index], dp[index - clients[j]] + costs[j])



```
