# 217. contains duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


#        brute force approach  TS: O(n2) SC: O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+ 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

#      another approach TS: O(nlogn) SC: O(1)
        # nums.sort()
        # n = len(nums)
        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False

# TS: O(n) SC: O(n) 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            
            hashset.add(n)
        
        return False

