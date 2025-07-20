def solution(board, h, w):
    return sum([1 if -1 < w+dx < len(board) and -1 < h+dy < len(board) and board[h][w] == board[h+dy][w+dx] else 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))])
