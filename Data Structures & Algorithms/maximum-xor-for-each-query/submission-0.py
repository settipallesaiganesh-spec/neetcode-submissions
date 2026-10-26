class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_num=(1<<maximumBit)-1
        xor=0
        for num in nums:
            xor^=num
        result=[]
        for i in range(len(nums)-1,-1,-1):
            result.append(xor^max_num)
            xor^=nums[i]
        return result 
        #Time and space is O(n) and O(n) respectively