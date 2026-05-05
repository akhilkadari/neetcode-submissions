import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        
        heap = [(-v, k) for k, v in map.items()]
        heapify = heapq.heapify(heap)
        
        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res