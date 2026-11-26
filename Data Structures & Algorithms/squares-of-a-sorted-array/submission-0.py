
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        res = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] ** 2
                left += 1
            else:
                res[pos] = nums[right] ** 2
                right -= 1

            pos -= 1

        return res
        #time and space is O(n) and O(n) respectively
