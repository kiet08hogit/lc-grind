# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder :
            return None
        root= preorder[0]
        rootnode= TreeNode(root)
        rootidx= inorder.index(root)

        inorder_left= inorder[: rootidx]
        inorder_right= inorder[rootidx+1:]

        leftsize= len(inorder_left)
        preorder_left= preorder[1: 1+leftsize]
        preorder_right = preorder[1+ leftsize:]
        rootnode.left= self.buildTree(preorder_left, inorder_left)
        rootnode.right= self.buildTree(preorder_right, inorder_right)
        return rootnode