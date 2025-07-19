# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        ind = inorder.index(root.val)
        r = len(inorder) - ind
        l = len(inorder) - r
        root.left = self.buildTree(preorder[1:1+l],inorder[0:l])
        root.right = self.buildTree(preorder[l+1:],inorder[ind+1:])
        return root