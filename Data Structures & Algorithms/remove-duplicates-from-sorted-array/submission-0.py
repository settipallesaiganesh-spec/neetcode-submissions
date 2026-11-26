
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1
        #time and space is O(n) and O(1) respectively
