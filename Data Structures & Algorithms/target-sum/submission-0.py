class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,total):
            if i==len(nums):
                if total==target:
                    return 1
                return 0
            if (i,total)in memo:
                return memo[(i,total)]
            add=dfs(i+1,total+nums[i])
            subtract = dfs(i + 1, total - nums[i])

            memo[(i, total)] = add + subtract

            return memo[(i, total)]

        return dfs(0, 0)
    #Time and space complexity is O(n*m ) and O(n*m ) respectively