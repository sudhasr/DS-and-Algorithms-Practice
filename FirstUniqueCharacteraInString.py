# 387. First Unique Character in a String

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
"""
Approach: Using HashMap
1. Create a HashMap, traverse the given string and update the HashMap with frequency
2. Traverse the string for the second time using enumerate function and check its frequency on the HashMap. Return the index of first string character whose frequency is 1.
"""
# Time Complexity - O(2N) where N is the length of string
# Space Complexity - O(N) for using hash map

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Edge Case
        if s == None or len(s) == 0:
            return -1
        mapp = dict()
        for i in range(len(s)):
            if s[i] not in mapp:
                mapp[s[i]] = 1
            else:
                mapp[s[i]] += 1
        for i,v in enumerate(s):
            if mapp[v] == 1:
                return i
        return -1