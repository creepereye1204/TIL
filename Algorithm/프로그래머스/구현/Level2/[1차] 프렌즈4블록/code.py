def s1(m, n, board):
    rst = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j+1] == board[i][j+1] == board[i+1][j] and board[i][j] != '.':
                rst.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
    return rst


def s2(temps, m, n, board):

    for y, x in temps:
        board[y][x] = '.'

    for idx, line in enumerate(list(zip(*board))):
        temp = ''.join(list(line))
        cnt = temp.count('.')
        k = list(cnt*'.'+temp.replace('.', ''))
        for o in range(len(list(zip(*board))[idx])):
            board[o][idx] = k[o]


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        temp = s1(m, n, board)
        answer += len(temp)
        if not temp:
            return answer
        s2(temp, m, n, board)
