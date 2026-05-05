# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l1 = prev

        curr = l2
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l2 = prev

        num1 = ""
        num2 = ""
        curr = l1
        curr2 = l2
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next
        
        sum = str(int(num1) + int(num2))
        dummy = res = ListNode()
        for c in sum:
            num = ListNode(int(c))
            res.next = num
            res = res.next

        curr = dummy.next
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
