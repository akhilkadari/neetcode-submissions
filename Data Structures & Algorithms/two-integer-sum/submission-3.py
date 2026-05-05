class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0
        for num in nums:
            map[num] = i
            i+=1
        for i, num in enumerate(nums):
            secondNum = target - num
            if secondNum in map and map[secondNum] != i:
                return [i, map[secondNum]]
                
                