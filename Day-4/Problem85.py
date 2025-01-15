# QUes Link:https://leetcode.com/problems/maximal-rectangle/description/

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        # Convert matrix elements to integers
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        def largestRectangleArea(heights):
            def nextSmallerElement(arr):
                stack = []
                result = [len(arr)] * len(arr)  
                for i in range(len(arr) - 1, -1, -1):
                    while stack and arr[stack[-1]] >= arr[i]:
                        stack.pop()
                    if stack:
                        result[i] = stack[-1]
                    stack.append(i)
                return result

            def prevSmallerElement(arr):
                stack = []
                result = [-1] * len(arr)  
                for i in range(len(arr)):
                    while stack and arr[stack[-1]] >= arr[i]:
                        stack.pop()
                    if stack:
                        result[i] = stack[-1]
                    stack.append(i)
                return result

            Nse = nextSmallerElement(heights)
            Pse = prevSmallerElement(heights)
            Max = 0
            for i in range(len(heights)):
                Max = max(Max, heights[i] * (Nse[i] - Pse[i] - 1))
            return Max
        
        # Initialize an array to store the "heights" for the histogram bars
        heights = [0] * len(matrix[0])
        max_area = 0
        
        for row in matrix:
            for i in range(len(row)):
                if row[i] == 0:
                    heights[i] = 0
                else:
                    heights[i] += 1
            # dp like approach in which we are using the previous calculated hieghts further
            # Calculate the maximal rectangle area for this row's histogram
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area
