
# https://leetcode.com/problems/two-sum/description/


# TC: O(n^2)
# SC: O(1)
# 1.      Brute force approach
from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# TC: O(n)
# SC: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            tempSum = target - nums[i]

            if tempSum in hashmap:
                return [hashmap[tempSum], i]
            
            hashmap[nums[i]] = i

        return []