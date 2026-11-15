
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]

            if right - left + 1 > k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
        #time and space is O(n) and O(k) respectively
