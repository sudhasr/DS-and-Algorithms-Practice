# 253. Meeting Rooms II

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

"""

"""
Approach1: Maintain a rooms array to store the end times
1. Sort the given array and write the edge cases - for no. of intervals 0 and 1
2. If number of intervals is greater than 1, add the end time of first interval in rooms array
3.
"""

# Time Complexity -
# Space Complexity - 

# class Solution:
#     def minMeetingRooms(self, intervals):
#         intervals.sort()
        
#         #Edge Case
#         if len(intervals) == 0:
#             return 0
#         if len(intervals) == 1:
#             return 1
                
#         rooms = [intervals[0][1]]
#         for i in range(1,len(intervals)):
#             if intervals[i][0] < rooms[i-1]:
#                 rooms.append(intervals[i][1])
#         return len(rooms)


import heapq
class Solution:
    def minMeetingRooms(self, intervals):        
        #Edge Case
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1
        intervals.sort()
        rooms = []
        #heapq.heapify(rooms)
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1,len(intervals)):
            if intervals[i][0] < rooms[0]:
                heapq.heappush(rooms, intervals[i][1])
            else:
                heapq.heappushpop(rooms, intervals[i][1])
        return len(rooms)

s = Solution()
print(s.minMeetingRooms([[1,5],[8,9],[8,9]]))