N, M = map(int, input().split(" "))
passwords = {}
for i in range(N):
    url, password = input().split(" ")
    passwords[url] = password
for i in range(M):
    url = input()
    print(passwords[url])
