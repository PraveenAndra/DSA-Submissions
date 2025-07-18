# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # l = 0
        # temp = head
        # while temp:
        #     temp = temp.next
        #     l += 1
        # n = l - n
        dummy = ListNode(0)
        dummy.next = head
        # temp = dummy
        # while n > 0:
        #     n -= 1
        #     temp = temp.next
        # temp.next = temp.next.next
        # return dummy.next
        second = head
        for i in range(n):
            second = second.next
        first = dummy
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
        