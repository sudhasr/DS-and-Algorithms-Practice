"""
Given a binary tree, imagine yourself standing on the left side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

--->		  1            
			/   \
--->	   2     3         
			\     \
--->		 5     4       

"""
# Approach1: BFS- Iterative approach using a queue
# 1. Do a level order traversal of the tree
# 2. At each level, add the first element of the queue to the result list

#Time Complexity: O(N) as we are processing every node of the tree
#Space Compelxity: O(k), where k is the max number of nodes at every level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #Edge Case
        if not root:
            return None
        # 1.
		result = []
        q = deque()
        q.append(root)
        while q:
			# 2.
            result.append(q[0].val)
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result