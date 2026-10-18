from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS=len(matrix), len(matrix[0])
        top, bottom=0, ROWS-1
        while top<=bottom:
            row= (top+ bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break
        if top > bottom:
            return False

        # Binary search within the selected row
        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[row][mid]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        #Time and space complexity is O(log(m* n)) and O(1) respectively