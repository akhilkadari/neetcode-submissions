# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
list 1: 1->2->4
list 2: 1->3->5
list 3: 3->6

1->1->2->3->3->4->5->6

Approach - Min Heap:
- the heap contains the smallest unprocessed node from each nonempty list
- because each list is sorted, no unprocessed node in that list can be smaller than its current head
- the min node in the heap is the smallest remaining node across ALL lists
- appending tha tnode maintain the outputs sorted order
- repeat this process until no nodes remain

Time complexity:
- initialize heap: O(nlogn)
- Across all lists we have K nodes
    - remove smallest node: O(logn)
    - insert successor: O(logn)
    - append the node to result O(1)
    - Cost: O(logn)
    - O(Klogn)
- O(nlogn + Klogn) -> O(Klogn)

Space Complexity:
- O(n)
'''


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for list_index, head in enumerate(lists):
            if head is not None:
                heapq.heappush(min_heap, (head.val, list_index, head))
        
        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            value, list_index, node = heapq.heappop(min_heap)

            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val, list_index, node.next))

            tail.next = node
            tail=tail.next
        tail.next = None

        return dummy.next










