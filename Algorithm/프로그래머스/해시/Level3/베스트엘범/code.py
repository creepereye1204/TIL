from collections import defaultdict


def solution(genres, plays):
    answer = []
    dict = defaultdict(list)
    ranks = defaultdict(int)
    for i in range(len(genres)):
        dict[genres[i]] += [(i, plays[i])]
        ranks[genres[i]] += plays[i]
    categories = sorted(ranks.items(), key=lambda x: -x[1])

    for category, _ in categories:
        sorted_values = sorted(dict[category], key=lambda x: (-x[1], x[0]))
        try:
            answer += [sorted_values[0][0]]
            answer += [sorted_values[1][0]]
        except:
            pass

    return answer
