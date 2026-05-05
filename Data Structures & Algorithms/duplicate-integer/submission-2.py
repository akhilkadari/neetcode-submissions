class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        
        for n in nums:
            if n in map:
                return True
            else:
                map[n] = 0
        return False