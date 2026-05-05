class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)-1):
            L, R = i+1, len(nums)-1
            
            while R > L:
                target = nums[R] + nums[L]
                if nums[i] + target == 0:
                    res.add((nums[i], nums[L], nums[R]))
                    L += 1
                    R -= 1
                elif nums[i] + target < 0:
                    L += 1
                else:
                    R -= 1
        return [list(i) for i in res]
