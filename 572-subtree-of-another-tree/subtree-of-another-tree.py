# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root,sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            if root.val != sub.val:
                return False
            return check(root.left,sub.left) and check(root.right,sub.right)
        
        q = deque([root])
        while q:
            temp = q.popleft()
            if temp and temp.val == subRoot.val:
                if check(temp,subRoot):
                    return True
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return False
        