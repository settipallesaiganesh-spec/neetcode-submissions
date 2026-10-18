
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    suffixes = dfs(end)

                    for suffix in suffixes:
                        if suffix:
                            sentences.append(word + " " + suffix)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)
        #TIme and space is O(n^3+ R) and O(n^2+ R) respectively
