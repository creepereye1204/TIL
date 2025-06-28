class HomeWork:
    curr_time = 0

    def __init__(self, name, start_time, time):
        m, s = map(int, start_time.split(':'))
        self.name = name
        self.start_time = 60*m+s
        self.time = int(time)


def solution(plans):

    stack = []
    answer = []
    homeworks = [HomeWork(*plan) for plan in plans]

    for homework in sorted(homeworks, key=lambda x: x.start_time):

        temp = homework.start_time-HomeWork.curr_time
        HomeWork.curr_time = homework.start_time
        while stack:
            if stack[-1].time <= temp:
                temp -= stack[-1].time
                answer.append(stack.pop().name)
            else:

                stack[-1].time -= temp
                break

        stack.append(homework)

    while stack:
        answer.append(stack.pop().name)

    return answer
