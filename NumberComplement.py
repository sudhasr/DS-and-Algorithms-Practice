# 476. Number Complement

"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

"""
Approach1: Without XOR
1. Find the number of bits of given number using division method
2. Find 2**bits-1 will give the largest value for that number of bits 
3. Subtract number from that value, it will give the complement
"""
# Time Complexity - O(bits)
# Space Complexity - O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        bits = 1
        n = num
        while n != 0 and n!= 1:
            n = n//2
            bits += 1
        return (2**bits)-1-num
		
"""
Approach2: With XOR
1. Find the number of bits of given number using division method
2. Find 2**bits-1 will give the largest value for that number of bits 
3. Find XOR of maximum value and the number, it will give the complement
"""
# Time Complexity - O(2*bits), for finding the bits and again for doing bit-wise XOR operation
# Space Complexity - O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        bits = 1
        n = num
        while n != 0 and n!= 1:
            n = n//2
            bits += 1
        return (2**bits)-1^num