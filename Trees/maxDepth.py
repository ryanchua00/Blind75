# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverseToRoot(root, 1)
    
    def traverseToRoot(self, root: TreeNode, depth: int) -> int:
        if root is None:
            return depth - 1
        return max(self.traverseToRoot(root.left, depth + 1), self.traverseToRoot(root.right, depth + 1))