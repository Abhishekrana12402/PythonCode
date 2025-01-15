# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Ques Link:https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
import sys
class Solution:
    from typing import Optional,TreeNode
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.Max=-sys.maxsize
        #Basic DFS  
        def Helper(node)->int:
            if not node:
                return 0
            left=Helper(node.left)
            right=Helper(node.right)
            left=max(0,left)
            right=max(0,right)
            # making sure no negative path contibutes so to get maximum path sum hence returning 0 if any -ve path found(neglecting that path)
            self.Max=max(self.Max,node.val+left+right)
            return max(left,right)+node.val
            # returning either the left branch or right branch (viz maximum) along with current node value
        Helper(root)
        return self.Max
    
        