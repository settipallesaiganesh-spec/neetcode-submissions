class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_beauty = 0

        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty

        res = []

        for q in queries:
            left, right = 0, len(items) - 1
            ans = 0

            while left <= right:
                mid = (left + right) // 2

                if items[mid][0] <= q:
                    ans = items[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1

            res.append(ans)

        return res
        #time and space is O(n*logn+  m*logn) and O(1) respectively