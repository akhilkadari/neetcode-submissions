# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                tmp = curr.next
                curr.next = None
                prev.next = tmp
                curr = tmp
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next

