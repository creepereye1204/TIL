N = int(input())

arr = [list(map(int, input().split(" "))) for _ in range(N)]

white = 0
blue = 0


def divide(arr, mid):
    global white, blue
    if check(arr) == 0:
        white += 1
        return
    elif check(arr) == 1:
        blue += 1
        return

    divide([g[:mid] for g in arr[:mid]], mid // 2)
    divide([g[mid:] for g in arr[:mid]], mid // 2)
    divide([g[:mid] for g in arr[mid:]], mid // 2)
    divide([g[mid:] for g in arr[mid:]], mid // 2)


def check(arr):
    if all(all(cell == 0 for cell in row) for row in arr):
        return 0
    elif all(all(cell == 1 for cell in row) for row in arr):
        return 1


divide(arr, N // 2)
print(white)
print(blue)
