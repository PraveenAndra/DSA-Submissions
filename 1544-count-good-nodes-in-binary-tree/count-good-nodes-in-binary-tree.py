# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,count,maxVal):
            if not node:
                return count
            if node.val >= maxVal:
                count += 1
                maxVal = node.val
            count = dfs(node.left,count,maxVal)
            count = dfs(node.right,count,maxVal)
            return count
        return dfs(root,0,float('-inf'))

        