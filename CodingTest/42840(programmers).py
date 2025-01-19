def solution(answers):
    result = []
    cnt = [0, 0, 0]
    a, b, c = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, value in enumerate(answers):
        if a[idx % 5] == value:
            cnt[0] += 1
        if b[idx % 8] == value:
            cnt[1] += 1
        if c[idx % 10] == value:
            cnt[2] += 1
    mx = max(cnt)

    for i in range(3):
        if cnt[i] == mx:
            result.append(i + 1)
    return result
