import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
해쉬도감 = {}
리스트도감 = [0]
for i in range(1, N + 1):
    포켓몬 = input().rstrip()
    해쉬도감[포켓몬] = i
    리스트도감.append(포켓몬)

for _ in range(M):
    포켓몬 = input().rstrip()
    try:
        print(해쉬도감[포켓몬])
    except:
        print(리스트도감[int(포켓몬)])
