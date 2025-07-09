
max_diff = -1 
answer = [-1] 

def solution(n, info):

    ryan_arrows = [0] * 11 

    find_best_shot(0, n, ryan_arrows, info) 

    return answer


def find_best_shot(idx, n_rem, ryan_arrows, apeach_info):
    global max_diff, answer

    
    if idx == 11:
        
        if n_rem > 0:
            ryan_arrows[10] += n_rem 
        
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            score_val = 10 - i
            if ryan_arrows[i] > apeach_info[i]:
                ryan_score += score_val

            elif apeach_info[i] > 0: 
                apeach_score += score_val
        
        
        current_diff = ryan_score - apeach_score
        
       
        if current_diff > 0:
            
            if current_diff > max_diff:
                max_diff = current_diff
                
                answer = ryan_arrows[:] 
           
            elif current_diff == max_diff:
               
                for i in range(10, -1, -1):
                    if ryan_arrows[i] > answer[i]:
                        answer = ryan_arrows[:]
                        break
                    elif ryan_arrows[i] < answer[i]: 
                        break
                   
        if n_rem > 0:
            ryan_arrows[10] -= n_rem 
        return

    needed_arrows_to_win = apeach_info[idx] + 1 


    if n_rem >= needed_arrows_to_win:
        ryan_arrows[idx] = needed_arrows_to_win

        find_best_shot(idx + 1, n_rem - needed_arrows_to_win, ryan_arrows, apeach_info)
        
        ryan_arrows[idx] = 0 
    

    find_best_shot(idx + 1, n_rem, ryan_arrows, apeach_info)
