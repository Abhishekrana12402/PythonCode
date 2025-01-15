# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Ques Link:https://leetcode.com/problems/validate-binary-search-tree/
from typing import Optional,TreeNode
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Helper(node,Max,Min)->bool:
            if not node:
                return True
            if Min and Max:
                if node.val<Max.val or node.val>Min.val:
                    return False
            if Min and node.val>=Min.val:
                return False
            if Max and node.val<=Max.val:
                return False
            return Helper(node.left,Max,node) and Helper(node.right,node,Min)
        return Helper(root,None,None)
        # Passing min and max and then updating it based on traversal if any given point of time it violates the BST rule i.e. left should be smaller and right should be greater then simply return False . So it will return false if any of the branch returns false
