# A연속이 긴 친구 +1 vs 노빠구 n
# mn과 mx 는 각각 오른쪽 왼쪽을 의미 나중에 2*mn+1+mx를 해야된다.그리고 연속횟수까지 저장할 cnt_mx까지
# A가 가장마뫃ㄴ이 연속되는 mn과mx를 찾기위해 좌표 start를 생성및 cnt변수로 연소 횟수화인
# 만약 A가 발견되고 cnt가 0이면 start변수현위치로 초기화cnt=1
# 만약 A가 발견되고 cnt가 0이 아니라면 cnt+=1
# 만약 A가 아니라면 지금까지의 cnt와 mx_cnt를 확인후 맞으면 mn,mx수정
def solution(name):
    ans = 0
    length = len(name)

    index = 0
    move = 1000000

    for i in range(length):
        ans += min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)
        index = i + 1

        while index < length and name[index] == "A":
            index += 1

        move = min(move, i * 2 + length - index)
        move = min(move, 2 * (length - index) + i)
    return move + ans
