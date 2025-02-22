flage = True


def move(x, y, d, r, c, board):
    global flage
    dx = [0, 0, -1, 1]  # 상하좌우 이동
    dy = [-1, 1, 0, 0]
    for i in range(1, 1001):
        x_ = x + dx[d - 1] * i
        y_ = y + dy[d - 1] * i
        if 0 <= x_ < c and 0 <= y_ < r and board[y_][x_]:
            board[y_][x_] = False  # 장애물 처리
            flage = True  # 움직였음을 표시
        else:
            return x + dx[d - 1] * (i - 1), y + dy[d - 1] * (i - 1)


def simulate(board, robot, dir, r, c):
    global flage
    flage = True
    x = robot[0]
    y = robot[1]
    board[y][x] = False  # 로봇의 초기 위치를 벽으로 설정
    while flage:
        flage = False
        for d in dir:
            x, y = move(x, y, d, r, c, board)

    return x, y


# 입력 처리
r, c = map(int, input().strip().split())
board = [[True] * c for _ in range(r)]
wall = int(input().strip())

for _ in range(wall):
    y, x = map(int, input().strip().split())
    board[y][x] = False  # 장애물 설정

# 로봇의 시작 위치
y, x = map(int, input().strip().split())
robot = [x, y]  # (x, y) 순서로 저장

# 방향 입력 (1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽)
dir = list(map(int, input().strip().split()))

# 시뮬레이션 실행
final_x, final_y = simulate(board, robot, dir, r, c)
print(final_y, final_x)  # 최종 위치 출력
