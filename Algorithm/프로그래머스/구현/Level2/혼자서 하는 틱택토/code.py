def solution(board):
    dic = {'O': 1, 'X': -1, '.': 0}
    rst = sum([dic[col] for row in board for col in row])

    if 0 <= rst <= 1:
        bingo = set([row for row in board])
        for col in zip(*board):
            bingo.add(''.join(col))
        bingo.add(board[0][0]+board[1][1]+board[2][2])
        bingo.add(board[2][0]+board[1][1] + board[0][2])

        if (rst == 0 and 'OOO' not in bingo) or (rst == 1 and 'XXX' not in bingo):
            return 1
    return 0
