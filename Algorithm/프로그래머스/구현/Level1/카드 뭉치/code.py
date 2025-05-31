
def solution(cards1, cards2, goal):
    for i in range(len(goal)):
        if cards1 and goal[i] == cards1[0]:
            cards1.pop(0)
        elif cards2 and goal[i] == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    return 'Yes'
