class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: 
                continue

            L = i+1
            R = len(nums)-1

            thirdNum = 0 - num
            while L < R:
                if nums[L] + nums[R] > thirdNum:
                    R-=1
                elif nums[L] + nums[R] < thirdNum:
                    L+=1
                else:
                    res.append([num, nums[L], nums[R]])
                    R-=1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                    
        return res
