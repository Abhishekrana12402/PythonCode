# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Ques Link:https://leetcode.com/problems/binary-tree-cameras/description/

import sys
from typing import Optional
class Solution:
    count=0
    def minCameraCover(self, root: Optional[TreeNode]) -> int: # type: ignore
        def Helper(node)->int:
            
            if not node:
                return 0
            if not node.left and not node.right:
                return -1
                # Basic DFS
            left=Helper(node.left)
            right=Helper(node.right)
            if left==-1 or right==-1:
                self.count+=1
                return 1
                # indicates that child is not watched hence need to install the camera at this particular node
            if left==1 or right==1:
                return 0
                # no need to install as current node is being captured by child node
            return -1      
        if Helper(root)==-1:
            return self.count+1
            # indicates theres no on to watch the root node hence need to install camera 
        return self.count
        
        