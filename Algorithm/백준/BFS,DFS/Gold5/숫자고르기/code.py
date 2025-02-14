# 먼저표를 테이블(딕셔너리) 변수로 구현
# 2 조합 A,B 로 나눔
# 두 조합이 길이가 다르면 조인 연산으로 해당되는 조합마노 봅자(0합집합)이후 테이블에서 갑시 치환하고 반복 아니면 조합 정렬후 리턴

n = int(input())
arr = [int(input()) for _ in range(n)]
table = {}
A = set()
B = set(arr)
for i in range(1, n + 1):
    table[arr[i - 1]] = i
    A.add(i)


def solve(A, B):
    global table
    if A == B:

        print(len(A))
        for i in sorted(list(A)):
            print(i)
        exit(0)
    C = A & B

    D = set()
    for c in C:
        D.add(table[c])
    solve(C, D)


solve(A, B)
