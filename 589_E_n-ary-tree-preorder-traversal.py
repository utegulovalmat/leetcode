"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            
            if not node:
                return None
            
            res.append(node.val)
            
            for c in node.children:
                dfs(c)
        
        dfs(root)
        return res