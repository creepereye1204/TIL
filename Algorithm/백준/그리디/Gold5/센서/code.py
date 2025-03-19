def solution(k, arr):
    answers = sorted(list(map(int, arr.split(' '))))
    return sum(sorted([answers[i]-answers[i-1] for i in range(1, len(answers))], reverse=True)[k-1:] if k-1 < len(answers) else [0])


input()
print(solution(int(input()), input()))
