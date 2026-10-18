class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,xor_total):
            if i==len(nums):
                return xor_total
            exclude=dfs(i+1,xor_total)
            include=dfs(i+1,xor_total^nums[i])
            return exclude+include
        return dfs(0,0)
        #Time and space is O(2^n) and O(n) respectively