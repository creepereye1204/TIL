def solution(survey, choices):
    scores = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for s, c in zip(survey, choices):
        score = c - 4
        if score != 0:
            key = "".join(sorted(s))
            scores[key] += score * (1 if s[0] in "RCJA" else -1)

    result = ""
    for types in ["RT", "CF", "JM", "AN"]:
        if scores[types] > 0:
            result += types[1]
        elif scores[types] < 0:
            result += types[0]
        else:
            result += types[0]
    return result
