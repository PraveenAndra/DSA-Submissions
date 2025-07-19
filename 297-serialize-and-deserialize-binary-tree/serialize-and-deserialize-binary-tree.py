# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        def dfs(node):
            nonlocal res
            if not node:
                res+= "None,"
                return 
            res += str(node.val)
            res += ","
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print(res)
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        if len(data) == 0 or data[0]==None:
            return None
        
        def dfs(data):
            if data[0] == "None":
                data.pop(0)
                return
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)
            
            

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))