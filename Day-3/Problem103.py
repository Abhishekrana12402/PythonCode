# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional,TreeNode
import sys
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[root]
        rev=True
        # to keep the track whether to add in reverse direction or normal
        List=[]
        if not root:
            return List
            # Normal BFS
        while  queue:
            inner=[]
            for i in range (len(queue)):
                node=queue.pop(0)
                inner.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if rev:
                List.append(inner)
            else:
                inner.reverse()
                List.append(inner)
                # reverse and then adding and then toggling the flag
            rev=not rev
        return List



        