# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        carry = 0
        res = 0
        temp = root
        while l1 or l2 or carry!=0:
            tot = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = tot // 10
            temp.next = ListNode(tot % 10)
            temp = temp.next
            l1,l2 = (l1.next if l1 else None),(l2.next if l2 else None)
        return root.next

