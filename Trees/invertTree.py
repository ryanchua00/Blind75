# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        if root.left is not None and root.right is not None:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left) 
            self.invertTree(root.right)
        elif root.left is not None:
            root.right = root.left
            root.left = None
            self.invertTree(root.right) 
        elif root.right is not None: 
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        return root