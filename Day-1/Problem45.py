# Ques Link:https://leetcode.com/problems/jump-game-ii/description/
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # initialising initial jump that can be taken with the first element
        step=nums[0]
        maxReach=nums[0]
        # maxReach will help in keeping the maximum value that can be choosen for minimum jump
        count=0
        jump=1
        if len(nums)==1:
            return 0
            # if length is 1 then frog itslef is at the last index 
        while(True):
            maxReach=max(maxReach,nums[count]+count)
            if(step==0):
                step=maxReach-count
                jump+=1
                # if steps becomes 0 then choose the maximum till now to minimize the jump required
            if(count+step>=len(nums)-1):
                return jump
                # indicates that we can reach the end with existing no. of jumps
            step-=1
            count+=1
            # incrementing the index as well as decrementing the step at each step