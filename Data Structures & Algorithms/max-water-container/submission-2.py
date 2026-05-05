class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        maxA = 0

        while L < R:
            area = abs(R-L) * min(heights[L], heights[R])
            maxA = max(area, maxA)

            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return maxA
        