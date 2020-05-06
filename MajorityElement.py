# 169. Majority Element

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
"""
Approach1: Using HashMap
1. Find the count of each numbers in the array and store it in a hashmap
2. Traverse the array and check if its count in the hashmap is greater than n/2
"""
# Time Complexity - O(N)
# Space Complexity - O(N)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mapp = dict()
        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = 1
            else:
                mapp[nums[i]] += 1
        for i in range(len(nums)):
            if mapp[nums[i]] > n/2:
                return nums[i]