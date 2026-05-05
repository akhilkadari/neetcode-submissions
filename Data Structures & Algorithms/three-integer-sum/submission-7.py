class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            L, R = i+1, len(nums)-1

            while L < R:
                target = nums[L] + nums[R]
                if nums[i] + target == 0:
                    res.add(tuple([nums[i], nums[L], nums[R]]))
                    L+=1
                    R-=1
                elif nums[i] + target > 0:
                    R-=1
                else:
                    L+=1

        return [list(i) for i in res]
