# Ques Link:https://leetcode.com/problems/search-a-2d-matrix/

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=0
        col=len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
        # Applying simple binary search by starting from right top and comparing the target 