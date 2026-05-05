class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        res.append(pre)
        for n in nums:
            if len(res) != len(nums):
                pre *= n
                res.append(pre)
        post = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
