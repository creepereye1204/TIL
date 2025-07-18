def convert(date):
    year, month, day = map(int, date.split('.'))
    return year*12*28+month*28+day


def solution(today, terms, privacies):
    answer = []
    today = convert(today)
    terms = {term.split(' ')[0]: int(term.split(' ')[1]) for term in terms}

    for idx, arr in enumerate(privacies):
        value, key = arr.split(' ')
        date = convert(value)+terms[key]*28
        if today >= date:
            answer.append(idx+1)

    return answer
