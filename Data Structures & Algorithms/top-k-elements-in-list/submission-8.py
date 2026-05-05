class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
        for n, cnt in map.items():
            freq[cnt].append(n)
         
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(res) < k:
                    res.append(n)
        return res


        
        return res
            

             

# key  value
# 1  : 3
# 2  : 2
# 3  : 1


               
