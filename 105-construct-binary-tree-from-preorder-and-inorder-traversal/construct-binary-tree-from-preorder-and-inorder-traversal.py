# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        ind = inorder.index(root_val)
        l,r  = ind, len(inorder) - ind - 1
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:1+l],inorder[0:ind]) if l > 0 else None
        root.right = self.buildTree(preorder[l+1::],inorder[ind+1::]) if r> 0 else None
        return root


         

        