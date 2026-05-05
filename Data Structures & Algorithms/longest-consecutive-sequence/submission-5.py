class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        sorted_nums = sorted(nums)
        print(sorted_nums)
        count = 1
        max_count = 1
        for i in range(len(sorted_nums)):
            if i+1 < len(sorted_nums):
                if sorted_nums[i+1] - sorted_nums[i] == 1:
                    count+=1
                if sorted_nums[i+1] - sorted_nums[i] == 0:
                    continue
                if sorted_nums[i+1] - sorted_nums[i] > 1:
                    count = 1
            max_count = max(count, max_count)
           
        return max_count
        