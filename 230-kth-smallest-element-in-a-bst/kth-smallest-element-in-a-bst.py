# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None
        def dfs(node):
            nonlocal count
            nonlocal res
            if not node or res:
                return 
            dfs(node.left)
            count -= 1
            print(count,node.val)
            if count==0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res



            

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
            
            
        