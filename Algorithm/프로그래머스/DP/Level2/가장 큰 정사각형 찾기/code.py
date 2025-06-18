
def solution(board):
    n = len(board)
    m = len(board[0])
    

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    
    
    answer = 0
    for i in range(n):
        temp = max(board[i])
        answer = max(answer, temp)
    
    return answer**2