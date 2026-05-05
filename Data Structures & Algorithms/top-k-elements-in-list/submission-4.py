class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = []
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n]+=1

        sorted_keys = sorted(map, key=lambda x: map[x], reverse=True)
            
        i=0
        while i < k:
            result.insert(0,sorted_keys[i])
            i+=1

        return result


# key  value
# 1  : 3
# 2  : 2
# 3  : 1


               
