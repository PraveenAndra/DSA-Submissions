# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 1
        def dfs(root,level):
            nonlocal max_depth
            max_depth = max(max_depth,level)
            if root:
                dfs(root.left,level+1)
                dfs(root.right,level+1)
        dfs(root,1)
        return max_depth-1
        