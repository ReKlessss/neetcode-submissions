# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        
        carry = 0
        while (l1 and l2) or carry > 0:
            res.next = ListNode()
            res = res.next

            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            summ = n1 + n2 + carry
            carry = 0

            if summ < 10:
                res.val = summ
            else:
                res.val = summ % 10
                carry += 1
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if l1:
            res.next = l1
        elif l2:
            res.next = l2


        return dummy.next