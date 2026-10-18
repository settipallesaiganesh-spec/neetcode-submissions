class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i in range(len(heights)+1):
            while stack and (i==len(heights)or heights[stack[-1]]>heights[i]):
                height=heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area