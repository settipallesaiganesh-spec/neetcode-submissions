class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1=sentence1.split()
        words2=sentence2.split()
        if len(words1)<len(words2):
            words1,words2=words2,words1
        left=0
        while left<len(words2) and words1[left]==words2[left]:
            left+=1
        right=0
        while right < len(words2) and words1[-1 - right] == words2[-1 - right]:
            right += 1

        return left + right >= len(words2)
        #TIme and space is O(n+m) and O(n+m) respectively