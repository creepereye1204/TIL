from collections import deque

dirs = dict()
folders, files = map(int, input().split(" "))


def find(query):

    cnt = []
    q = deque([query])
    while q:
        dir = q.popleft()

        for value in dirs[dir]:

            if value not in dirs:
                cnt += [value]
            else:
                q += [value]
    return cnt


for i in range(folders + files):
    key, value, is_folder = map(str, input().split(" "))

    if key not in dirs:

        dirs[key] = []
    if value not in dirs and is_folder == "1":
        dirs[value] = []

    dirs[key] += [value]


q = int(input())
for _ in range(q):
    query = input().split("/")[-1]

    files = find(query)

    print(len(set(files)), len(files))
