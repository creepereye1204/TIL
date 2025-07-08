def solve(visited, cards, i):
    cnt = 0
    while not visited[i]:
        visited[i] = True
        cnt += 1
        i = cards[i]
    return cnt


def solution(cards):
    cards = [0]+cards
    l = len(cards)

    visited = [False]*(l)
    answer = []
    for i in range(1, l):
        if not visited[i]:
            answer.append(solve(visited, cards, i))

    if len(answer) > 1:
        answer.sort()
        return answer[-1]*answer[-2]
    return 0
