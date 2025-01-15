# Ques Link:https://leetcode.com/problems/first-missing-positive/
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        index=0
        while index<len(nums):
            correctpos=nums[index]-1
            #  1's correct index is 0 ,2's is 1 .... so applying cyclic sort to arrange no.s serially and check if the element is in given range or not
            if 1 <= nums[index] <= len(nums) and nums[index]!=nums[correctpos]:
                nums[index],nums[correctpos]=nums[correctpos],nums[index]
                # placing element at their respective position
            else:
                index+=1
        print(nums)
        for i in range (len(nums)):
            if nums[i]!=i+1:
                return i+1
                # validating the odd one out or one who is not at correct position
        return len(nums)+1