# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_lookup = {}
        for ind,val in enumerate(inorder):
            inorder_lookup[val] = ind
        preorder_ind = 0
        def construct(left,right):
            nonlocal preorder_ind
            if left > right:
                return None
            root_val = preorder[preorder_ind]
            root = TreeNode(root_val)
            preorder_ind += 1
            root.left = construct(left,inorder_lookup[root_val]-1)
            root.right = construct(inorder_lookup[root_val]+1,right)
            return root
        
        return construct(0,len(preorder)-1)
         

        