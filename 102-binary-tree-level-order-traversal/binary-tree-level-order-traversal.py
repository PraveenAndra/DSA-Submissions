# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = []
        if not root:
            return res
        stack.append(root)
        while stack:
            temp = []
            temp_res = []
            for node in stack:
                temp_res.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(temp_res)
            stack = temp
        return res





        