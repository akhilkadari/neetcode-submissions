class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while L < R:
            mid = (L+R) // 2
            if nums[mid] > nums[R]:
                L = mid+1
            else:
                R = mid\

        l, r = 0, len(nums) - 1

        if target >= nums[L] and target <= nums[r]:
            l = L
        else:
            r = L - 1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        
       

        
        return -1