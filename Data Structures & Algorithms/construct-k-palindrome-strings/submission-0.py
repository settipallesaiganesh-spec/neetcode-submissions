
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd_count = 0

        for count in freq:
            if count % 2 == 1:
                odd_count += 1

        return odd_count <= k
        #time and space is O(n) and O(1) respectively