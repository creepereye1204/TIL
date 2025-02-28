words = input()
for i in range(len(words)):
    if words[i:] == words[i:][::-1]:
        print(len(words) + i)
        exit(0)
