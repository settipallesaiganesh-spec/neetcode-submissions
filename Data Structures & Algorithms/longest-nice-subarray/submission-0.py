class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left=0
        bits=0
        res=0
        for right in range(len(nums)):
            while bits & nums[right]:
                bits^=nums[left]
                left+=1
            bits|=nums[right]
            res=max(res,right-left+1)
        return res
        #TIme and space is O(n) and O(1) respectively