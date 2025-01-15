# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Ques Link:https://leetcode.com/problems/binary-tree-right-side-view/description/
from collections import deque


class Solution:
    from typing import TreeNode,List,Optional
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans=[]
        queue=deque([root])
        # initialsing queue as well as list 
        while(queue):
            size=len(queue)
            for i in range(size):
                temp=queue.popleft()
                # when we reach the last index at each level we will add it to our result
                if i==size-1:
                    ans.append(temp.val)
                    # appending the left node
                if temp.left:
                    queue.append(temp.left)
                    # appending the right side
                if temp.right:
                    queue.append(temp.right)
        return ans
        