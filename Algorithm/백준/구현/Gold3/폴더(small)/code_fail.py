N, M = map(int, input().split(" "))
dirs = [["main", []]]
files = []


def mkdir(parent, child, cur_dir):

    for dir in cur_dir:
        if type([]) == type(dir):
            if dir[0] == parent:
                dir[1] += [[child, []]]
                return
            else:
                mkdir(parent, child, dir)


def mkfile(parent, child, cur_dir):

    for dir in cur_dir:
        if type([]) == type(dir):
            if dir[0] == parent:
                dir[1] += [child]
                return
            else:
                mkfile(parent, child, dir)


def find(path, cur_dir):

    if not path:

        return cur_dir

    for dir in cur_dir:

        if type([]) == type(dir) and dir[0] == path[0]:

            return find(path[1:], dir[1])


def counter(cur_dir):

    for dir in cur_dir:
        if type([]) != type(dir):
            global files
            files += [dir]
        else:
            counter(dir[1])


for _ in range(N + M):
    parent, child, dir_or_file = map(str, input().split(" "))
    if dir_or_file == "1":
        mkdir(parent, child, dirs)
    else:
        mkfile(parent, child, dirs)

q = int(input())

for _ in range(q):
    query = list((input()).split("/"))

    path = find(query, dirs)
    counter(path)
    print(len(files), len(set(files)))
    files = []
