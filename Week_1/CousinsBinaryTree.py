# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        foundNode = []
        
        def search(parent, node, depth):
            if node is None:
                return
            
            if node.val==x or node.val==y:
                foundNode.append((depth,parent))
            
            search(node, node.left, depth+1)
            search(node, node.right, depth+1)
        
        search(None, root, 0)    
        return foundNode[0][0]==foundNode[1][0] and foundNode[0][1]!=foundNode[1][1]
        
        
        