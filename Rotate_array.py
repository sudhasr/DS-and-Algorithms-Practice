# 189. Rotate Array
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""

"""
Approach1: Reversing approach
1. Reverse the given array 
2. Reverse the reversed array from index 0 to k-1
3. Reverse the reversed array elements from index k to end
"""

# Time COmplexity - O(n)
# Space Complexity - O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Edge Case
        if nums == None or len(nums)==0:
            return 0
        if k == 0:
            return
        # What if k is greater than size of the array
        k = k % len(nums)
        
        # Reversing the entire array
        self.swap(nums, 0, len(nums)-1)
        # Performing reverse on the reversed array until index k-1
        self.swap(nums, 0, k-1)
        # Performing reverse on the reversed array from index k to end
        self.swap(nums, k, len(nums)-1)
        return nums
        
    def swap(self, array, first, last):
        while first < last:
            array[first], array[last] = array[last], array[first]
            first += 1
            last -= 1

