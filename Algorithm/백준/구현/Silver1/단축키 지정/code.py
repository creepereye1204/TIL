short_key = set([])
n = int(input())

for _ in range(n):
    vocas = list(map(str, input().split(" ")))
    toggle = True
    rst = []
    for voca in vocas:

        if voca[0].upper() not in short_key and toggle:
            toggle = False
            short_key.add(voca[0].upper())

            voca = voca.replace(voca[0], "[" + voca[0] + "]", 1)
        rst += [voca]
    if toggle:
        rst = []
        for voca in vocas:

            for v in voca[1:]:

                if v.upper() not in short_key and toggle:
                    toggle = False
                    short_key.add(v.upper())

                    voca = voca[0] + voca[1:].replace(v, "[" + v + "]", 1)
                    break
            rst += [voca]
    print(" ".join(rst))
