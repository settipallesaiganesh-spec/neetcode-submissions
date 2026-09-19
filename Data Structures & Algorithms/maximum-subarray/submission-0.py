class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=0
        maxSum=nums[0]
        for num in nums:
            curSum=max(curSum+num, num)
            maxSum=max(maxSum, curSum)
        return maxSum
        #Time and space is O(n) and O(1) respectively