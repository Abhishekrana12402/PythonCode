# Ques Link:https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    from typing import List
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list=[]
        if not nums:
            return [-1,-1]
            # empty array
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=start+(end-start)//2
            if(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        if start>=0 and start<len(nums) and nums[start]==target:
            list.append(start)
        else:
            return [-1,-1]
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=start+(end-start)//2
            print(mid)
            if(nums[mid]<=target):
                start=mid+1
            else:
                end=mid-1
        list.append(end)
        
        return list
        # apllying binary search 2 times to get the start and end of the target For the very first time applying < sign to the first index of the target value then using <= to move pratition to the last index of the target
        
            