# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Ques Link:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
class Solution:
    from typing import TreeNode
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS Application
        def Helper(node,p,q)->'TreeNode': # type: ignore
            if not node:
                return None
            left=Helper(node.left,p,q)
            right=Helper(node.right,p,q)
            if node==p or node==q:
                return node
                # if i found any of the node just return the node (p or q)
            if left and right:
                return node
                # if i am getting both left and right means current node is my LCA Similarly if found left return left and if found right return right
            if left:
                return left
            if right:
                return right
            return None
        return Helper(root,p,q)
        