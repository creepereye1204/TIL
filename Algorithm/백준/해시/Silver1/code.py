# 방문자들을 set에 저장후 처음같과 마지막 값이 같을떄까지 순회
index = 0


def solve(start, end):
    global visited, students
    visited.add(end)
    if start == end:
        return
    solve(start, students[end])


while True:
    rst = 0
    visited = set()
    index += 1
    T = int(input())
    if T == 0:
        break
    students = {}
    for _ in range(T):
        a, b = map(str, input().split(" "))
        students[a] = b
    for key in students.keys():
        if key not in visited:
            rst += 1
            solve(key, students[key])
    print(index, rst)
