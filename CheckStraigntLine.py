# 1232. Check If It Is a Straight Line

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""

"""
Approach:


"""

# Time Complexity - O(N)
# Space Complexity - O(1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Edge Case
        if len(coordinates) == 2:
            return True
        
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x1 - x0) * (y - y1)  != (x - x1) * (y1 - y0):
                return False
        return True