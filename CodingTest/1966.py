t = int(input())
for _ in range(t):
    answer = 0
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    while arr:

        if max(arr) == arr[0]:
            arr.pop(0)
            answer += 1
            if m == 0:
                print(answer)
                break
        else:
            v = arr.pop(0)
            arr.append(v)
        m = (m - 1) % len(arr)
