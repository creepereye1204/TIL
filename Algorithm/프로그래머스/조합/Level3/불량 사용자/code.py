def solution(user_id, banned_id):
    answer = 0
    import re
    from itertools import permutations
    answers = []
    banned_id = [id.replace('*', '.') for id in banned_id]
    for p in permutations(user_id, len(banned_id)):
        cnt = 0
        for i in range(len(p)):
            if re.match(banned_id[i], p[i]) and len(banned_id[i]) == len(p[i]):
                cnt += 1
        if cnt == len(banned_id):
            p = sorted(p)
            if p not in answers:
                answers.append(p)

    answer = len(answers)

    return answer
