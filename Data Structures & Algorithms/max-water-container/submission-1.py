class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        L, R = 0, len(heights)-1

        while L < R:
            area = abs(R-L) * min(heights[L], heights[R])
            maxA = max(maxA, area)

            if heights[R] < heights[L]:
                R-=1
            else:
                L+=1
        return maxA
            