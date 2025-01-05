def get_pos(number, keyboard):
    for i in range(4):
        for j in range(3):
            if number == keyboard[i][j]:
                return i, j


def get_len(a1, a2, b1, b2):
    return abs(a1 - a2) + abs(b1 - b2)


def solution(numbers, hand):
    left_pos = [3, 0]
    right_pos = [3, 2]

    result = ""

    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["", 0, ""]]
    for number in numbers:
        y, x = get_pos(number, keyboard)

        if number in [2, 5, 8, 0]:
            L = get_len(left_pos[0], y, left_pos[1], x)
            R = get_len(right_pos[0], y, right_pos[1], x)

            if L > R:
                right_pos[0], right_pos[1] = y, x
                result += "R"
            elif L < R:
                left_pos[0], left_pos[1] = y, x
                result += "L"
            else:
                if hand == "left":
                    left_pos[0], left_pos[1] = y, x
                    result += "L"
                else:
                    right_pos[0], right_pos[1] = y, x
                    result += "R"

        elif number in [1, 4, 7]:
            left_pos[0], left_pos[1] = y, x
            result += "L"
        else:
            right_pos[0], right_pos[1] = y, x
            result += "R"

    return result
