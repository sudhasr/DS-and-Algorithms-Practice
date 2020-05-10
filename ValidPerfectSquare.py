# 367. Valid Perfect Square

"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

"""
"""
Approach: Binary Search
1. Keep low to be 1 and high to be the num. Find the mid element.
2. If square of mid is equal to the num, return True. 
3. If the square of mid is greater than num then it means we need to reduce our search space from high to mid-1
4. If the square of mid is lower than the num then we need to reduce search space from low to mid+1  

"""
# Time Complexity - O(logN)
# Space Complexity - O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Edge Case
        if num == 0:
            return False
        low = 1
        high = num
        while low <= high:
            mid = low + (high - low)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid-1
            else:
                low = mid+1
        return False