# 1.스패이스 변수르 ㄹ사용해서 스패이스가 나왔으면 True로이후 로 스패이스가 ㅇ나니 무자를 만다면 이때 체인지후 space는 false
# 이후 계속 문자가 나오다 갑자기 스패이스가 나오면 ture
def solution(texts):
    space = True
    ans = ""
    for text in texts:
        temp = ""
        if space:
            if text.isalpha():
                temp = text.upper()
                space = False
            elif text == " ":
                temp = text
            else:
                temp = text
                space = False
        else:
            if text == " ":
                temp = text
                space = True
            elif text.isalpha():
                temp = text.lower()
            else:
                temp = text
        ans = ans + temp

    return ans
