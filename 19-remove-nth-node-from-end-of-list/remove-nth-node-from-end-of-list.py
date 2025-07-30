# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        for i in range(n+1):
            temp = temp.next
        second = dummy
        while temp:
            temp = temp.next
            second = second.next
        second.next = second.next.next
        return dummy.next

        