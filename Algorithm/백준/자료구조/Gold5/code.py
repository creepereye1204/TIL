from collections import deque


def cal(arr, query):
    front = True
    while query:
        q = query.popleft()
        if q == "R":
            front = not front
        else:

            if not arr or arr[0] == "":
                print("error")
                return
            if front:
                arr.popleft()
            else:
                arr.pop()

    if not front:
        arr.reverse()
    print("[" + ",".join(arr) + "]")


for _ in range(int(input())):
    query = deque(list(input()))

    input()
    arr = input()[1:-1].split(",")
    arr = deque(arr)
    cal(arr, query)
