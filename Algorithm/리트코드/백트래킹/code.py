from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([[beginWord, 1]])
        while q:
            cur_word, cnt = q.popleft()
            if cur_word == endWord:
                return cnt
            for i in range(len(cur_word)):
                for c in "".join([chr(i) for i in range(ord("a"), ord("z") + 1)]):
                    next_word = cur_word[:i] + c + cur_word[i + 1 :]
                    if next_word in wordSet:
                        q += [[next_word, cnt + 1]]
                        wordSet.remove(next_word)

        return 0
