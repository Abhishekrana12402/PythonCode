# Ques Link:https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        if nums[start]<nums[end]:
            return nums[start]
        while start<end:
            mid=start+(end-start)//2
            if nums[mid]>nums[end]:
                start=mid+1
                # means search in the right half
            elif nums[mid]<nums[end]:
                end=mid
                # smallest is in the left half so ignore right half
            else:
                end-=1
                
        return nums[end]