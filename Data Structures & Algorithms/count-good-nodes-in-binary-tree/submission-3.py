# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, prev_max):
            count=0
            next_max= prev_max
            if node.val >= next_max:
                count+=1
                next_max=node.val
            if node.left:
                count+=dfs(node.left,next_max)
            if node.right:
                count+=dfs(node.right,next_max)
            return count
        return dfs(root, root.val)