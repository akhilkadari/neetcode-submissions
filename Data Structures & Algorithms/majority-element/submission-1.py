class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 0

        for n in nums:
            if res != n:
                count -= 1
            if count == 0:
                res = n 
            count += 1
        return res
