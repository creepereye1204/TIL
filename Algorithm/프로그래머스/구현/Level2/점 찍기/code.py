import math

def solution(k, d):
    answer = 0

    d_squared = d * d
    
    for x in range(0, d + 1, k):
        val_for_sqrt = d_squared - (x * x)

        max_y = int(math.sqrt(val_for_sqrt))
        
        
        answer += (max_y // k) + 1
        
    return answer
