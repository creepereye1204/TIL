HEX= "0123456789ABCDEF"
def convert(number,base):
    global HEX
    div,mod=divmod(number,base)
    if div==0:
        return HEX[mod]
    else:
        return convert(div,base)+ HEX[mod]
def solution(n, t, m, p):
    answer = ''
    num=0
    while len(answer)<t*m:
        answer=answer+convert(num,n)
        num+=1
    return answer[:t*m][p-1::m]