def solution(surveies, choices):
    answer = ''

    dic = {'RT': {'T': 0, 'R': 0}, 'CF': {'C': 0, 'F': 0},
           'JM': {'J': 0, 'M': 0}, 'AN': {'A': 0, 'N': 0}}
    for survey, choice in zip(surveies, choices):
        key = ''.join(sorted(list(survey)))
        dic[key][survey[0]] += max(4-choice, 0)
        dic[key][survey[1]] += max(choice-4, 0)
    for key in dic.keys():
        arr = []
        for k, v in dic[key].items():
            arr.append((-v, k))
        answer = answer+sorted(arr)[0][1]
    return answer
