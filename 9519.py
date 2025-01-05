ans = []


def make(x, l, n):
    global ans

    # 길이가 짝수면
    if l % 2 == 0:
        string = list(x[i] for i in range(l // 2))
        for i in range(0, l, 2):  # 0, 2, 4
            string.insert(i + 1, x[-(i + 1) // 2])  # 1, 3, 4 / 0, 1, 2

    # 길이가 홀수면
    else:
        string = list(x[i] for i in range(l // 2 + 1))
        for i in range(0, l - 1, 2):
            string.insert(i + 1, x[-(i + 1) // 2])

    ans.append("".join(string))
    if "".join(string) == target:
        return ans
    else:
        return make(string, l, n - 1)


def solution(N, target, l):
    make(target, l, l)
    period_len = len(ans)
    return ans[period_len - N % period_len - 1]


N = int(input())
target = input()
l = len(target)

print(solution(N, target, l))
