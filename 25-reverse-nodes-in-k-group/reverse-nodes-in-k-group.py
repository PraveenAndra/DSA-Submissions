# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # temp = head
        # for i in range(k):
        #     if not temp:
        #         return head
        #     temp = temp.next
        # prev = None
        # curr = head
        # for i in range(k):
        #     next = curr.next
        #     curr.next = prev
        #     prev= curr
        #     curr = next
        # head.next = self.reverseKGroup(temp,k)
        # return prev
        temp = head
        newHead = None
        prevTail = None
        while temp:
            ptr = temp
            count = 0
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count == k:
                prev = None
                curr = temp
                while curr and count > 0:
                    next = curr.next
                    curr.next = prev
                    prev =curr
                    curr =next
                    count -= 1
                if not newHead:
                    newHead = prev
                if prevTail:
                    prevTail.next = prev
                prevTail = temp
                temp = ptr
            
            else:
                if prevTail:
                    prevTail.next = temp
                break

        return newHead if newHead else head