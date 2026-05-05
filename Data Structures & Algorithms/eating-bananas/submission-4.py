class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        while L <= R:
            k = (L+R) // 2

            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h:
                res = k
                R = k - 1
            else:
                L = k+1
        return res




            

            