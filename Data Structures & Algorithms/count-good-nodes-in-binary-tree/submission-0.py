# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev_max):
            res = 0
            next_max = prev_max
            if node.val >= prev_max:
                res += 1
                next_max = node.val
            if node.left:
                res += dfs(node.left, next_max)
            if node.right:
                res += dfs(node.right, next_max)
            return res
        
        return dfs(root, root.val)