def solve(sub_text,board):
    if not sub_text:
        return
    word,idx=sub_text[0]
    left=[(word_,idx_) for word_,idx_ in sub_text if idx_<idx]
    right=[(word_,idx_) for word_,idx_ in sub_text if idx_>idx]
    board[idx]=word
    if all(board):
        for t in board:
            if True!=t:
                print(t,end='')
        print()
        
    solve(right,board)
    solve(left,board)

def solution(text):
    
    board=[True]*100
    stack=sorted([(text[i],i) for i in range(len(text))],key=lambda x:(x[0],x[1]))
    solve(stack,board)
    answer = 0
    return answer

solution(input())