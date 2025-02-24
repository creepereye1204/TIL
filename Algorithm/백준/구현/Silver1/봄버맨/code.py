# n이 홀수면 'o'만 출력햐ㅐ
# 그래프를 입력크기대로 만들어준다
# 이때 공기를 '.'로 표시

# 폭탄이 터지게 만들고 이때 터질때 'o' 인곳만 터지고
# 타질때 방향이 '.'일떄만 터진다
# 터진곳은 'X'로 만들어
# 이후 보드를 X 전부 '.'으로 만든다.
# 반대로 '.'은 'o'으로 만들고 이걸 반복한다
# n까지
# 보여 줄때는 'X'를 전부 폭탄으로 바꾼다.

r, c, n = map(int, input().split(" "))
graph = [list(input()) for _ in range(r)]


def rollback(graph):
    global r, c
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "X":
                graph[i][j] = "."
            else:
                graph[i][j] = "O"


def run(graph, x, y):
    global r, c
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    graph[y][x] = "X"
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if 0 <= x_ < c and 0 <= y_ < r and graph[y_][x_] == ".":
            graph[y_][x_] = "X"


if n % 2 == 0:
    for i in range(r):
        for j in range(c):
            print("O", end="")
        print()
    exit(0)
else:
    for _ in range(n // 2):
        for i in range(r):
            for j in range(c):
                if graph[i][j] == "O":
                    run(graph, j, i)
        rollback(graph)

for i in range(r):
    for j in range(c):
        print(graph[i][j], end="")
    print()
