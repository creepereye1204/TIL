def solution(players, m, k):
    answer = 0
    servers = []
    for i in range(24):

        total = players[i]//m
        cnt = 0
        for j in range(len(servers)):
            servers[j] -= 1
            if servers[j] > 0:
                cnt += 1

        while total > cnt:
            answer += 1
            cnt += 1
            servers.append(k)

    return answer
