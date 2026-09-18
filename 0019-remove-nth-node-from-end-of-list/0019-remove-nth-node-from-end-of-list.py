# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        c = 0
        crr = head
        while crr is not None:
            c += 1
            crr = crr.next
        
        p = c - n

        if p == 0:
            return head.next

        crr = head

        for i in range(p - 1):
            crr = crr.next

        crr.next = crr.next.next

        return head

