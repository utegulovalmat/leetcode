# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def trim(node, lo, hi):
            if not node:
                return None
            
            if hi < node.val:
                return trim(node.left, lo, hi)
            
            elif node.val < lo:
                return trim(node.right, lo, hi)
            
            else:
                node.left = trim(node.left, lo, hi)
                node.right = trim(node.right, lo, hi)
                return node
            
        return trim(root, low, high)