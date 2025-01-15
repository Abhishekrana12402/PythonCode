# Ques Link:https://leetcode.com/problems/continuous-subarray-sum/description/
class Solution:
    from typing import List
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {}
        sum=0
        map[0]=-1
        for i in range (len(nums)):
            sum+=nums[i]
            if sum%k in map and i-map[sum%k]>=2:
                return True
                # storing the modulo part of the sum in the map which will help in keeping records of whether the multiple of k exists or not also check the length of subarray found
            if sum%k not in map:
                map[sum%k]=i
        # for key, value in map.items():
        #     print(f"{key}: {value}")
        return False