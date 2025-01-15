# Ques Link:https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


class Solution:
    from typing import List
    def search(self, nums: List[int], target: int) -> int:
        def FindPivot(arr:List[int])->int:
            left,right=0,len(arr)-1
            while(left<right):
                mid=(left+right)//2
                if arr[mid]>arr[right] :
                    left=mid+1
                else:
                    right=mid
            return left; 

        def BS(arr:List[int],start,end)->int:
            while(start<=end):
                mid=(start+end)//2
                if(arr[mid]==target):
                    return mid
                elif arr[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return -1
        pivot=FindPivot(nums)
        print(pivot)
        if nums[pivot]==target:
            return pivot
        elif(pivot==0):
            return BS(nums,0,len(nums)-1)
        elif(target>=nums[0]):
            return BS(nums,0,pivot)
        else:
            return BS(nums,pivot+1,len(nums)-1)
            
        


    