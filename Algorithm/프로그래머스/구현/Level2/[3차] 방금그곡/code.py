class Music:
    def __init__(self, idx, length, title, value):
        self.idx = idx
        self.length = length
        self.title = title
        self.value = value


def solution(m, musicinfos):
    for t in ['C#', 'D#', 'F#', 'G#', 'A#', 'B#']:
        m = m.replace(t, t[0].lower())
    musics = {}
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, value = musicinfo.split(',')
        start = int(start[:2])*60+int(start[3:])
        end = int(end[:2])*60+int(end[3:])
        length = end-start

        for t in ['C#', 'D#', 'F#', 'G#', 'A#', 'B#']:
            value = value.replace(t, t[0].lower())
        div, mod = divmod(length, len(value))
        value = value*div+value[:mod]

        if m in value:

            if title not in musics:
                musics[title] = Music(idx, length, title, value)
            else:
                musics[title].length += length

    answer = list(musics.values())
    answer.sort(key=lambda x: (-x.length, x.idx))
    if answer:
        return answer[0].title
    return '(None)'
