from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    data = defaultdict(list)
    for i in info:
        info_parts = i.split()
        score = int(info_parts[-1])
        conditions = info_parts[:-1]
        for k in range(5):
            for combo in combinations(range(4), k):

                key_list = ['-'] * 4
                for idx in combo:
                    key_list[idx] = conditions[idx]

                key = tuple(key_list)
                data[key].append(score)

    results = []

    for q in query:
        q_parts = q.replace('and ', '').split()
        q_score = int(q_parts[-1])
        q_conditions = tuple(q_parts[:-1])
        scores_for_key = data[q_conditions]
        idx = bisect_left(scores_for_key, q_score)
        results.append(len(scores_for_key) - idx)

    return results
