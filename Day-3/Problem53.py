# Ques Link:https://leetcode.com/problems/maximum-subarray/description/
import sys
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left=0
        right=0
        Max=-sys.maxsize
        for i in range (len(nums)):
            if left<0:
                left=0
            left+=nums[i]
            Max=max(left,Max)
        for i in range (len(nums)-1,-1,-1):
            if right<0:
                right=0
            right+=nums[i]
            Max=max(right,Max)
        return Max
        # there are two possibilities either we can get max from left side or else right side so keep on calculating from both the end and return the max from both side. If addition with new number will reduce the ans then dont consider it. i.e. reduce to 0 if answer goes beyond 0
