# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        BOTH_DONE = 0
        BOTH_PENDING = 2
        LEFT_DONE = 1
        stack = [(root,2)]
        ind = -1
        one_found = False
        while stack:
            parent,state = stack[-1]
            if state != BOTH_DONE:
                if state == BOTH_PENDING:
                    if p.val == parent.val or q.val == parent.val:
                        if one_found:
                            return stack[ind][0]
                        else:
                            one_found = True
                            ind = len(stack) - 1
                    child = parent.left
                else:
                    child = parent.right
                stack.pop()
                stack.append((parent,state-1))
                if child:
                    stack.append((child,BOTH_PENDING))
            else:
                if one_found and ind == len(stack) - 1:
                    ind -= 1
                stack.pop()
        return None






