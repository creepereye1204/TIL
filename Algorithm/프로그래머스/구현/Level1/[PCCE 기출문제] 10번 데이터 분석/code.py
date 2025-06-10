def solution(datas, ext, val_ext, sort_by):
    answer = []
    category = ["code", "date", "maximum", "remain"]
    key1 = category.index(ext)
    key2 = category.index(sort_by)

    for data in datas:
        if data[key1] < val_ext:
            answer.append(data)

    return sorted(answer, key=lambda x: x[key2])
