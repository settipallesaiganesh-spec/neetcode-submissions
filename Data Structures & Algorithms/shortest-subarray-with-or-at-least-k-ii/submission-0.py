from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 32
        left = 0
        ans = float('inf')

        def update(num, val):
            for b in range(32):
                if num & (1 << b):
                    bits[b] += val

        def get_or():
            result = 0
            for b in range(32):
                if bits[b] > 0:
                    result |= (1 << b)
            return result

        for right in range(n):
            update(nums[right], 1)

            while left <= right and get_or() >= k:
                ans = min(ans, right - left + 1)
                update(nums[left], -1)
                left += 1

        return ans if ans != float('inf') else -1