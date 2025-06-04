def solution(board, moves):
    board = [[a for a in arr[::-1] if a != 0] for arr in list(zip(*board))]
    stack = []
    answer = 0
    for move in moves:
        num = move-1
        if board[num]:
            if stack and board[num][-1] == stack[-1]:
                board[num].pop()
                stack.pop()
                answer += 2
            else:
                stack.append(board[num].pop())
    return answer
