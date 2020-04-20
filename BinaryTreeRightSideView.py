#199. Binary Tree Right Side View

"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""

# Approach1: BFS- Iterative approach using a queue
# 1. Do a level order traversal of the tree
# 2. At each level, add the last element of the queue to the result list

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
            result.append(q[-1].val)
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
		

""" Approach2: DFS recursive approach using a queue
1. Have depth variable and compare it with the size of result array as we move down the tree (pre-order traversal). When they are equal, add the value to result.
2. When we hit the leaf node and move to previous recursive call, we got to right child. This time size of result will be greater than depth. Update the right child value 
	at the depth index of result array.
"""
#Time Complexity: O(N) as we are processing every node of the tree
#Space Compelxity: O(k), where k is maxDepth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # Edge Case
        if root == None:
            return []
        
        result = []
        # DFS recursive function
        self.__dfs(root, 0, result)
        return result
        
        
    def __dfs(self, node, depth, result):
        # Base Case
        if node == None:
            return
        # Comparing depth avlue with size of result array
        if len(result) == depth:
            result.append(node.val)
        else:
            # Update the right element
            result[depth] = node.val
            
        if node.left:
            self.__dfs(node.left, depth+1, result)
        if node.right:
            self.__dfs(node.right, depth+1, result)