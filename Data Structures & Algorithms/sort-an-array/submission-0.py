import heapq 
class Solution:
    """
    Idea: build a max heap from the array, then repeatedly move the largest element to the end
    and shrink the heap

    - max heap -> access the current largest element in O(1) and restore heap order
    in O(log n) after each pop

    - n = len(nums)
    - 1. To build a heap is O(n) using heapify
    - 2. Extract max repeatedly -> n - 1
        - swap root with the last unsorted element
        - shrink heap size
        - heapify root
        - each heapify is O(log n) -> done n times
    - 3. time complexity -> O(nlogn)
    
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sorted_res = []

        while nums:
            smallest_value = heapq.heappop(nums)
            sorted_res.append(smallest_value)

        return sorted_res
        
        