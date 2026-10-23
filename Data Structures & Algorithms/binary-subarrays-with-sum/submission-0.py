class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k):
            if k<0:
                return 0
            left=0
            count=0
            result=0
            for right in range(len(nums)):
                count+=nums[right]
                while count>k:
                    count-=nums[left]
                    left+=1
                result+=right-left+1
            return result
        return atMost(goal)-atMost(goal-1)
        #TIme and space is O(n) and O(1) respectively