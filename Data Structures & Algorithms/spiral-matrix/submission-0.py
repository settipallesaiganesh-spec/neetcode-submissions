class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        while left<=right and top<=bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse right column from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Traverse bottom row from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Traverse left column from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res