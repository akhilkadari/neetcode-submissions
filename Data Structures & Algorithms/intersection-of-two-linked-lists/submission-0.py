# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        currA = headA

        while currA:
            seen.add(currA)
            currA = currA.next

        currB = headB
        intersect = 0
        while currB:
            if currB in seen:
                return currB
            currB = currB.next

        return None                