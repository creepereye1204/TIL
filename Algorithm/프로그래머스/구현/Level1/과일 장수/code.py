def solution(k, m, score):
    score.sort(reverse=True)
    return sum([m*score[i] for i in range(m-1, len(score), m)])
