class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum=max(nums)
        left=0
        count=0
        result=0
        for right in range(len(nums)):
            if nums[right]==maximum:
                count+=1
            while count>=k:
                if nums[left]==maximum:
                    count-=1
                left+=1
            result+=left
        return result
        #TIme and space is O(n) and O(1) respectively