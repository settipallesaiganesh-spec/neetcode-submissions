
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans
    #Time and space is O(n) and O(1) respectively
