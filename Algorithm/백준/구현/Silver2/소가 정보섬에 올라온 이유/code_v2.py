N, Q = map(int, input().split())
score = list(map(int, input().split()))
numbers = list(map(int, input().split()))
pre_score = [0] * N
for i in range(N):
    pre_score[i] = score[i % N] * score[(i + 1) % N] * score[(i + 2) % N] * score[(i + 3) % N]
pre_SUM = sum(pre_score)
for num in numbers:
    for i in range(4):
        pre_score[num - i - 1] = -pre_score[num - i - 1]
        pre_SUM += 2 * pre_score[num - i - 1]
    print(pre_SUM)
