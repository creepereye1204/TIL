def check(n):
    # n을 만들 수 있는 제곱수들을 구해줌
    nums = []
    for i in range(int(n**0.5), 0, -1):
        nums.append(i**2)

    # 최소 개수가 1개인 경우
    if n == nums[0]:
        return 1

    # 최소 개수가 2개인 경우
    for i in nums:
        if n - i in nums:
            return 2

    for i in nums:
        for j in nums:
            if n - i - j in nums:
                return 3
    return 4


n = int(input())
print(check(n))
