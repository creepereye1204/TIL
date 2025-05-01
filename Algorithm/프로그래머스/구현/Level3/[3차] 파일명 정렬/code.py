def convert(filename):
    HEAD = ''
    NUMBER = ''
    for t in filename:
        if HEAD and NUMBER and not t.isdigit():
            break
        else:
            if not t.isdigit():
                HEAD = HEAD+t
            elif t.isdigit():
                NUMBER = NUMBER+t
    return HEAD.lower(), str(int(NUMBER))


class File:
    def __init__(self, filename, head, number, index):
        self.head = head
        self.number = int(number)
        self.filename = filename
        self.index = index


def solution(files):
    answer = []
    group = {}
    for file in files:
        head, number = convert(file)
        key = head+number
        if key in group:
            group[key] += 1
        else:
            group[key] = 0
        answer.append(File(file, head, number, group[key]))
    answer.sort(key=lambda x: (x.head, x.number, x.index))

    return [file.filename for file in answer]
