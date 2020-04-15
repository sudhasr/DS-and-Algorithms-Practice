"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
"""

 """ Approach1: BFS- Iterative using Queue and In-degrees array
1. Create an in-degrees array of the size = numCourses. In-degrees means number of nodes coming IN the node represented by index of in-degrees array.
2. Use BFS approach, create a queue and push all those nodes whose in-degrees is zero(0).
	Those courses whose in-degree is zero means either they dont have any pre-req or their pre-reqs are done.
	Push those nodes into the queue whose in-degrees is zero. It means that this course if it is a pre-req for another course(s),
	makes it possible to now take that course(s). 
3. After pushing into queue, traverse throught the prerequisites list to find its dependency nodes and reduce the in-degrees of those
	dependency nodes by 1 in the in-degrees array. 
4. After reducing by 1, check if the value has become zero, if it is, then push it to queue
5. Once queue is empty, we are done processing all nodes. Check if any value in in-degrees array is greater than zero.If yes, return False.
	If all the values are equal to zero, then return True
"""

#Time Complexity: O(4N) as we repeated traverse prerequisites and in-degrees array 
#Space Compelxity: O(N) for the in-degrees array

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        # 1.
        indegrees = [0  for i in range(numCourses)]
        for i in range(len(prerequisites)):
            indegrees[prerequisites[i][0]] += 1
        
        # 2.
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        # 3.
        while q:
            course = q.popleft()
            for i in range(len(prerequisites)):
                if prerequisites[i][1] == course:
                    indegrees[prerequisites[i][0]] -= 1
					# 4.
                    if indegrees[prerequisites[i][0]] == 0:
                        q.append(prerequisites[i][0])
        # 5.
        for i in range(len(indegrees)):
            if indegrees[i] > 0:
                return False
        return True