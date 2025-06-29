# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # covered = {None}
        # res = 0
        # def dfs(node,par = None):
        #     nonlocal res
        #     if node:
        #         dfs(node.left,node)
        #         dfs(node.right,node)
        #         if (par is None and node not in covered) or node.left not in covered or node.right not in covered:
        #             res += 1
        #             covered.update({node,node.left,node.right,par})
        # dfs(root)
        # return res
        # 0 ffor not covered 1 for camera 2 for covered
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return float('inf')
            left = dfs(node.left)
            right = dfs(node.right)
            curr = min(node.left.val if node.left else float('inf'),node.right.val if node.right else float('inf'))
            if curr == 0:
                res += 1
                node.val = 1
            elif curr == 1:
                node.val = 2
        dfs(root)
        return res+(1 if root.val == 0 else 0)


        