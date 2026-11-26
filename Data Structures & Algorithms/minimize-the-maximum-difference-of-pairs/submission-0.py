class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 0

            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2
                else:
                    i += 1

                if count >= p:
                    return True

            return False

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if can_form_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return left
        #time and space is O(n*logn+ n*logD) and O(1) respectively