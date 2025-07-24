# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(left,right):
            head = ListNode()
            merged = head
            while left or right:
                if not left:
                    merged.next = right
                    right = right.next
                elif not right:
                    merged.next = left
                    left = left.next
                else:
                    if left.val < right.val:
                        merged.next = left
                        left = left.next
                    else:
                        merged.next = right
                        right = right.next 
                merged = merged.next
            return head.next        
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        first = lists[0]
        for i in lists[1::]:
            first = mergeTwoLists(first,i)
        return first
        