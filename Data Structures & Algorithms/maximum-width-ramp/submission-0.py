class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack=[]
        for i,num in enumerate(nums):
            if not stack or num<nums[stack[-1]]:
                stack.append(i)
        max_width=0
        for j in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[j]:
                i=stack.pop()
                max_width=max(max_width,j-i)
        return max_width
        #TIme and space is O(n) and O(n) respectively