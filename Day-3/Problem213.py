# Ques Link:https://leetcode.com/problems/house-robber-ii/description/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def Rob(start,end):
            prev1=0
            prev2=0
            for i in range (start,end):
                temp=prev1
                prev1=max(prev2+nums[i],prev1)
                prev2=temp
            return prev1
        if len(nums)==1:
            return nums[0]
        return max(Rob(0,len(nums)-1),Rob(1,len(nums)))
        # similar to house robber-1 just we need to make suree if first element is contributing to our answer then not to include the last one as it will be adjacent vice versa
