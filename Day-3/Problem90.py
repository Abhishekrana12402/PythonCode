# Ques Link:https://leetcode.com/problems/subsets-ii/description/
class Solution:
    from typing import List
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list=[[]]
        nums.sort()
        start=0
        size=0
        for i in range (len(nums)):
           
            if i>0 and nums[i]==nums[i-1]:
                start=size
            else:
                start=0
            size=len(list)
            for j in range(start,len(list)):
                new=list[j]+[nums[i]]
                list.append(new)
        return list
        
        #   [[],[1]]
        #   [[],[1],[2],[1,2]]
        #   [[],[1],[2],[1,2],[2,2],[1,2,2] there can be repetation in subsets hence we will ignore the subset viz already been made in previous steps and focus on the new one as each step the length keeps on doubling hence we will use the prev end as start to generate new subsets 
       
        