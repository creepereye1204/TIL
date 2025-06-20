def hanoi(f, t, m, n):
    if n == 0:
        return []

    return hanoi(f, m, t, n-1) + [[f, t]] + hanoi(m, t, f, n-1)


def solution(n):
    return hanoi(1, 3, 2, n)