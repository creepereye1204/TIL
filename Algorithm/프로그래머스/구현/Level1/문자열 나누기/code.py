def solution(s):
    answer = 0
    text = ''
    for i in range(len(s)):
        if not text:
            text = s[i]
            a = 1
            b = 0
        else:
            if text != s[i]:
                b += 1
            else:
                a += 1
            if a == b:
                text = ''
                a = b = 0
                answer += 1
    return answer if a == b else answer+1
