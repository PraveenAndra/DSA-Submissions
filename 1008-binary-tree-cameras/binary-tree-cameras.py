# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0
        covered = {None}
        def dfs(node,parent=None):
            nonlocal ans
            if node:
                dfs(node.left,node)
                dfs(node.right,node)
                if (parent is None and node not in covered) or (node.left not in covered or node.right not in covered):
                    ans += 1
                    covered.update({node,node.left,node.right,parent})
        dfs(root)
        return ans
        

        