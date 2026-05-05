class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res = 0

        # for L in range(len(heights)):
        #     for R in range(L+1, len(heights)):
        #         area  = (R-L) * min(heights[R],heights[L])
        #         res = max(res, area)
        # return res
        res = 0
        L = 0
        R = len(heights)-1

        while L < R:
            area = (R-L) * min(heights[R], heights[L])
            res = max(res, area)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return res
        

        