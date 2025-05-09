def solution(n):

    triangle = [[0] * n for _ in range(n)]
    answer = []
    y, x = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):

            # Down
            if i % 3 == 0:
                y += 1

            # Right
            elif i % 3 == 1:
                x += 1

            # Up
            else:
                y -= 1
                x -= 1

            triangle[y][x] = num
            num += 1

    for i in range(n):
        for j in range(i+1):
            answer.append(triangle[i][j])

    return answer
