import heapq

class Solution:
    # approach
    '''
    - create a hashmap containing each number and its frequency
    - heapify the hashmap as a min heap -> loop over heap k times and return the top k elements within the heap
    - negate each value so it acts as a max heap
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)

        max_heap = [(-v, k) for k, v in map.items()]
        heapq.heapify(max_heap)

        res = []
        for i in range(k):
            freq, num = heapq.heappop(max_heap)
            res.append(num)
        return res
        
        