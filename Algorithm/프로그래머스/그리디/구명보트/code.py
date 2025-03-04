from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        a = people.popleft()
        while people:
            b = people.pop()
            answer += 1
            if a + b <= limit:
                break
        else:
            answer += 1
    return answer
