N = int(input())
int_lst = list(map(int, input().split()))
cal_lst = list(map(int, input().split()))

mx, mn = -1e12, 1e12


def do_dfs(n, cal):
    global mx, mn
    if n == N - 1:
        mx, mn = max(mx, cal), min(mn, cal)

    if cal_lst[0] != 0:
        cal_lst[0] -= 1
        do_dfs(n + 1, cal + int_lst[n + 1])
        cal_lst[0] += 1

    if cal_lst[1] != 0:
        cal_lst[1] -= 1
        do_dfs(n + 1, cal - int_lst[n + 1])
        cal_lst[1] += 1

    if cal_lst[2] != 0:
        cal_lst[2] -= 1
        do_dfs(n + 1, cal * int_lst[n + 1])
        cal_lst[2] += 1

    if cal_lst[3] != 0:
        cal_lst[3] -= 1
        do_dfs(n + 1, int(cal / int_lst[n + 1]))
        cal_lst[3] += 1


do_dfs(0, int_lst[0])
print(mx)
print(mn)
