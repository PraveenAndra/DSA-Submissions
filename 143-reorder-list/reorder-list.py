# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        curr = mid
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        left,right = head,prev
        while right.next:
            left.next, left = right, left.next
            right.next,right = left, right.next



        