# 입력 받을때 MBTI 배열을 2X4로 만든다
# 이후 set에 저장
# 거리 계산 함수로 가장 짧은 3개의 거리를 찾는다
# 이때 배열을 콤비네이션으로 뽑아서 각 MBTI 2배열을 set의 길이로 카운트
from itertools import combinations
from collections import defaultdict


def calc(arr):
    mn = 100000000
    for a in list(combinations(arr, 3)):
        cnt = 0

        c = set()

        for x, y, z in list(zip(*a)):

            c.add(x)
            c.add(y)
            c.add(z)

            if len(c) == 1:
                pass
            else:
                cnt += 2
            c = set()

        mn = min(mn, cnt)
    return mn


T = int(input())
for _ in range(T):
    n = int(input())
    MBTIS = input().split(" ")
    MBTI_ARR = []
    check = defaultdict(int)
    for MBTI in MBTIS:
        arr = [0] * 4

        if MBTI[0] == "E":
            arr[0] = 1

        if MBTI[1] == "S":
            arr[1] = 1
        if MBTI[2] == "T":
            arr[2] = 1
        if MBTI[3] == "J":
            arr[3] = 1
        if check[str(arr)] < 3:
            MBTI_ARR += [tuple(arr)]
            check[str(arr)] += 1

    print(calc(MBTI_ARR))
