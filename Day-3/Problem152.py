# Ques Link:-https://leetcode.com/problems/maximum-product-subarray/description/
import sys
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left=1
        right=1
        Max=-sys.maxsize
        for i in range (len(nums)):
            if left==0:
                left=1
            left*=nums[i]
            Max=max(left,Max)
        for i in range (len(nums)-1,-1,-1):
            if right==0:
                right=1
            right*=nums[i]
            Max=max(right,Max)
        return Max
        # there are two possibilities either we can get max from left side or else right side so keep on calculating from both the end and return the max from both side. If multiplication with new number will reduce the ans then dont consider it
