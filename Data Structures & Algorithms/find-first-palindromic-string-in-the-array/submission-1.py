
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word

        return ""
        #time and space is O(n*m) and O(m) respectively