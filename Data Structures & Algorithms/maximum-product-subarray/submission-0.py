class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=nums[0]
        cur_min=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            temp_max=max(num,num*cur_max,num*cur_min)
            cur_min=min(num, num*cur_max,num*cur_min)
            cur_max=temp_max
            result=max(result,cur_max)
        return result
        #Time and space is O(n) and O(1) respectively