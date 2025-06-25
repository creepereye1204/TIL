def solve(level, diffs, times, limit):
    if diffs[0] > level:
        return False
    limit -= times[0]
    for i in range(1, len(diffs)):
        if level >= diffs[i]:
            limit -= times[i]
        else:
            limit -= ((times[i-1]+times[i])*(diffs[i]-level)+times[i])

    return limit >= 0


def solution(diffs, times, limit):
    answer = []
    start = 1
    end = max(diffs)
    while start <= end:

        level = (start+end)//2
        if solve(level, diffs, times, limit):
            answer.append(level)
            end = level-1
        else:
            start = level+1

    return min(answer)
