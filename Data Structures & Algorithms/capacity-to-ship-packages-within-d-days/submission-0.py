class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            required_days=1
            current_weight=0
            for weight in weights:
                if current_weight+weight>mid:
                    required_days+=1
                    current_weight=0
                current_weight+=weight
            if required_days>days:
                left=mid+1
            else:
                right=mid
        return left
        #TIme and space is O(n*logS) and O(1) respectively