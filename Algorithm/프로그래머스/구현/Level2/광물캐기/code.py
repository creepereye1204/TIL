from collections import deque


def solution(picks, minerals):
    answer = 0
    dic = {"diamond": 25, "iron": 5, "stone": 1}
    minerals = [dic[mineral] for mineral in minerals[:sum(picks)*5]]
    minerals = deque(sorted([minerals[i:i+5] for i in range(0,
                     len(minerals), 5)], key=lambda x: (-max(x), -sum(x))))
    picks = deque([0]*picks[0]+[1]*picks[1]+[2]*picks[2])
    while picks and minerals:
        pick = picks.popleft()
        mineral = minerals.popleft()
        if pick == 0:
            answer += len(mineral)
        elif pick == 1:
            answer += mineral.count(25)*5+len(mineral)-mineral.count(25)
        else:
            answer += mineral.count(25)*25+mineral.count(5)*5+mineral.count(1)
    return answer
