# 252. Meeting Rooms

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true

"""

"""
Approach: 
1. Sort the intervals and compare every start time with its previous end time
2. If the start time of an interval is lesser than the end time of previous interval, then return false
3. If all the intervals satisfy the above condition to have start time greater than end time of previous interval, then return True.
"""

# Time Complexity - O(NlogN) as sorting time complexity dominates the O(N) comparison
# Space Complexity - O(1)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals with respect to the start time
        intervals.sort()
        
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True