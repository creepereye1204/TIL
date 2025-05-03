def s1(m, n, board):
    bingo = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j+1] == board[i][j+1] == board[i+1][j] and board[i][j] != '.':
                bingo.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
    return bingo


def s2(bingo, board, m):

    for y, x in bingo:
        board[y][x] = '.'

    for idx, line in enumerate(list(zip(*board))):
        temp = ''.join(list(line))
        cnt = temp.count('.')
        k = list(cnt*'.'+temp.replace('.', ''))
        for i in range(m):
            board[i][idx] = k[i]
    return len(bingo)


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while bingo := s1(m, n, board):
        answer += s2(bingo, board, m)
    return answer
