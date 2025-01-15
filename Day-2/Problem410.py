# Ques Link:https://leetcode.com/problems/split-array-largest-sum/description/
import sys
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        # initialsing low with maximum no. in the array because of which array can be split in the maximum parts and the high with sum because its the no. that will split the array int minimum parts which is 1
        def BS(low,high,arr)->int:
            while low<=high:
                mid=(low+high)//2
                print(mid)
                status=Check(mid,nums)
                # checking the status and based on which shifting the partition
                if status>k:
                    low=mid+1
                else:
                    high=mid-1
            return low
        # check splitting of the array based on our choosen no which is mid if we are able to split the array in more then expected parts then we need to increase the no. so to decrease the splitting upto k and vice versa
        def Check(mid,arr)->int:
            sum=0
            count=1
            for i in range(len(arr)):
                sum+=arr[i]
                if sum>mid:
                    sum=arr[i]
                    count+=1
            return count
        return BS(low,high,nums)

