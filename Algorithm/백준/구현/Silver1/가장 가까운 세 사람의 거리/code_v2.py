from itertools import combinations


def distance(lst):
    A_B, B_C, C_A = 0, 0, 0
    for i in range(4):
        if lst[0][i] != lst[1][i]:
            A_B += 1
        if lst[1][i] != lst[2][i]:
            B_C += 1
        if lst[2][i] != lst[0][i]:
            C_A += 1
    return A_B + B_C + C_A


def solution(N, mbti):
    if N > 32:
        return 0  # 이부분만 추가해주면 된다.
    Min = 1e9
    for lst in combinations(mbti, 3):
        Min = min(distance(lst), Min)
    return Min


T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    print(solution(N, mbti))
