# Ques Link:https://leetcode.com/problems/sort-colors/
class Solution:
    from typing import List
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j,k=0,0,len(nums)-1
        while(i<=j and j<=k):
            if nums[j]==0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
            elif nums[j]==1:
                j+=1
            
            else:
                temp=nums[j]
                nums[j]=nums[k]
                nums[k]=temp
                k-=1
                # Make use of 3 pointers 1 for tracking 0,1 for 1 and 1 for 2 and making swaps based on the value and terminating the loop once the rule is violated viz i<=j<=k (it indicates that array has been perfectly sorted)
        