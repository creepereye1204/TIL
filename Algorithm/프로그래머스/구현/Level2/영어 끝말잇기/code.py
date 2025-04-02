def solution(n, words):
    word_set = set([words[0]])
    for index in range(1, len(words)):
        word = words[index]
        if word not in word_set and words[index-1][-1] == words[index][0]:
            word_set.add(word)
        else:
            return [1+(index) % n, 1+(index)//n]
    return [0, 0]
