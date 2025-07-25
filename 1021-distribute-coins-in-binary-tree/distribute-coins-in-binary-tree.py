# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        def dfs(node):
            nonlocal moves
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left)+abs(right)
            return (node.val-1)+left+right 
        dfs(root)
        return moves
            
            



        