def solution(numbers):
    return str(int("".join(list(map(str, sorted(numbers, key=lambda num: str(num) * 3, reverse=True))))))
