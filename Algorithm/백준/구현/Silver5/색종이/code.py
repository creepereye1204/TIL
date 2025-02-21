n = int(input())
rst = 0
board = [[0] * (101) for _ in range(101)]
for i in range(n):
    a, b = map(int, input().split(" "))
    for y in range(b, b + 10):
        for x in range(a, a + 10):

            board[y][x] = 1

for y in range(101):
    for x in range(101):
        rst += board[y][x]

print(rst)
