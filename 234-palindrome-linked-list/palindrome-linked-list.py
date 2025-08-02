# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        curr = slow.next
        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
        result = True
        first = head
        second = prev
        while result and second:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next
        return result


        