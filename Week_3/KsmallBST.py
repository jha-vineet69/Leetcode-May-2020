# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    out = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(root,k)
        return self.out
    
    def inorder(self, root, k):
        if root.left!= None:
            self.inorder(root.left,k)
        
        self.count+=1
        if(self.count==k):
            self.out = root.val
            return
        
        if root.right!= None:
            self.inorder(root.right,k) 