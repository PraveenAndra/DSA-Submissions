# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # postorder = postorder[::-1]
        # print(postorder)
        ind = 0
        inorder_lookup = {}
        for ind,val in enumerate(inorder):
            inorder_lookup[val] = ind 
        def construct(left,right):
            if left > right:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root.right = construct(inorder_lookup[root_val]+1,right)
            root.left = construct(left,inorder_lookup[root_val]-1)
            return root
        return construct(0,len(postorder)-1)