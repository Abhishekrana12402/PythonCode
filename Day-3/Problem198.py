# Ques Link:https://leetcode.com/problems/house-robber/
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0
        for items in nums:
            temp=prev1
            prev1=max(prev2+items,prev1)
            prev2=temp
        return prev1
        # using two previous we can keep track of non adjacent items if adding the current item still gets you lesser value then the other previous then its beneficial to keep the previous greater one rather then new item (acts like greedy approach)
