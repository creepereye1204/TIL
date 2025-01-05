def get_len(args):
    return (
        abs(args[0][0] - args[1][0]) + abs(args[0][1] - args[1][1]) + abs(args[1][0] - args[2][0]) + abs(args[1][1] - args[2][1])
    ) - (abs(args[0][0] - args[2][0]) + abs(args[0][1] - args[2][1]))


def solution(points):
    total = 0
    answer = -1
    for i in range(len(points) - 1):
        total += abs(points[i][0] - points[i + 1][0]) + abs(points[i][1] - points[i + 1][1])

    for i in range(len(points) - 2):
        args = [
            [points[i][0], points[i][1]],
            [points[i + 1][0], points[i + 1][1]],
            [points[i + 2][0], points[i + 2][1]],
        ]
        answer = max(answer, get_len(args))
    return total - answer


x = int(input())
points = [list(map(int, input().split(" "))) for _ in range(x)]
print(solution(points))
