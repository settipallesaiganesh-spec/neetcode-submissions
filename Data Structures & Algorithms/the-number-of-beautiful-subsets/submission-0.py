from typing import List
from collections import Counter

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = 0
        freq = Counter()

        def backtrack(index):
            nonlocal count

            if index == len(nums):
                count += 1
                return

            # Skip the current index
            backtrack(index + 1)

            # Include the current value if valid
            x = nums[index]

            if freq[x - k] == 0 and freq[x + k] == 0:
                freq[x] += 1
                backtrack(index + 1)
                freq[x] -= 1

        backtrack(0)

        # Exclude the empty subset
        return count - 1
        #Time and space is O(2^n) and O(n) respectively