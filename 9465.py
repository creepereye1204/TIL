T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    arr.append(list(map(int, input().split(" "))))
    arr.append(list(map(int, input().split(" "))))
    d = [[0] * (N) for _ in range(2)]
    d[0][0] = arr[0][0]
    d[1][0] = arr[1][0]
    try:
        d[0][1] = d[1][0] + arr[0][1]
        d[1][1] = d[0][0] + arr[1][1]

        for i in range(2, N):
            d[0][i] = max(d[1][i - 1], d[1][i - 2]) + arr[0][i]
            d[1][i] = max(d[0][i - 1], d[0][i - 2]) + arr[1][i]
    except:
        pass
    print(max(d[0][N - 1], d[1][N - 1]))
