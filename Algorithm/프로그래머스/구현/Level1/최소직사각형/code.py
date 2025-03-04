def solution(sizes):
    temp = []
    for size in sizes:
        temp.append([max(size), min(size)])
    return sorted(temp, key=lambda x: (-x[0]))[0][0] * sorted(temp, key=lambda x: (-x[1]))[0][1]
