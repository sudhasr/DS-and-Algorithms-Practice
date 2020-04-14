"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Approach1: Iterative approach using a queue
# 1. Create a queue (useful here because of its FIFO property) and enque the root into it (only root element is present at 1st level)
# 2. Until the queue is not empty, we calculate size of the queue(size will be equal to number of nodes at each level), process the elements one by one for that size
# 3. First append it to level list, check if the node being processed has a left and right child, if it has, then push them to the end of queue		
# 4. After processing each level, add the temp list to the result list. 

#Time Complexity: O(N) as we are processing every node of the tree
#Space Compelxity: O(k), where k is the max number of nodes at every level in the queue, O(N) if we consider the result list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #Edge Case
        if root == None:
            return []      
        # 1.
        result = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
			# 2.
            size = len(queue)
			# 3.
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
			# 4.
            result.append(level)
        return result