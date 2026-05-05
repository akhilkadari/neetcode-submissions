class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i, n in enumerate(nums):
            secondNum = target - n
            if secondNum in map:
                return [map[secondNum], i]
            map[n] = i