keyboard = [
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
    ["z", "x", "c", "v", "b", "n", "m"],
]

# 초기 위치 설정
# 반복문으로 다음키 설정
# 해당 왼오 구분
# 거리 구하기
# 현재위치 갱신
# 거리 저장


def get_len(x1, y1, x2, y2):
    # 거리 반환
    return abs(x1 - x2) + abs(y1 - y2)


def get_position(word):
    # (y,x) 반환
    for i in range(3):
        if word in keyboard[i]:
            return (i, keyboard[i].index(word))


def get_is_left(y, x):

    if (y < 2 and x < 5) or (y == 2 and x < 4):
        return True
    return False


def solution(SL, SR, text):
    answer = 0
    SLP = get_position(SL)
    SRP = get_position(SR)

    for t in text:
        y, x = get_position(t)
        if get_is_left(y, x):

            z = get_len(SLP[0], SLP[1], y, x)
            SLP = (y, x)
            answer += z
        else:
            z = get_len(SRP[0], SRP[1], y, x)
            SRP = (y, x)
            answer += z

    return answer + len(text)


L, R = input().split(" ")
text = input()
print(solution(L, R, text))
