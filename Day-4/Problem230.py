# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Ques Link:https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
from typing import List,Optional,TreeNode

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def Helper(node):
            if not node:
                return 0
            Helper(node.left)
            self.count+=1
            if self.count==k:
                self.ans=node.val
                return
            Helper(node.right)
            # in simple in order traversal we are able to track in ascending as rule of BST therefore by keeping the track of count we can easily track the nth smallest element
            
        self.ans=0
        self.count=0
        Helper(root)
        return self.ans