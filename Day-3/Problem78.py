# Ques Link:-https://leetcode.com/problems/subsets/description/
class Solution:
    from typing import List
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list=[[]]
        
        for i in range (len(nums)):
            subset=[]
            for j in list:
                InnerList=j.copy()
                InnerList.append(nums[i])
                subset.append(InnerList)
            list.extend(subset)
        return list
        #  [[]]
        #   [[],[1]]
        #   [[],[1],[2],[1,2]]
        #   [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] we are using the prev subset for mking the new one hence we just need to copy the ith index and insert the new element
        