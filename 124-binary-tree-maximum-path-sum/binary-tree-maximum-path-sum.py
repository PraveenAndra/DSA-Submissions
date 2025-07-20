# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            res = max(res,left+right+node.val)
            return max(left+node.val,right+node.val)
        dfs(root)
        return res

        