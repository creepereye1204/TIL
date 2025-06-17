def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    si = [sum([d % i for d in data[i-1]]) for i in range(row_begin, row_end+1)]
    answer = si[0]
    for s in si[1:]:
        answer ^= s
    return answer
