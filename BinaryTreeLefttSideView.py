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

# Approach1: DFS- Recursive approach
# 1. Have a depth variable and compare it with siz eof result array
# 2. Add values to the result only if that level is processed of rthe first time, meaning, len(result) == depth
# 3. Dont do anything when len(result) > depth. It means we have already processed left mpst node of the level

#Time Complexity: O(N) as we are processing every node of the tree
#Space Compelxity: O(k), where k is the maxDepth

		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
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
            
        if node.left:
            self.__dfs(node.left, depth+1, result)
        if node.right:
            self.__dfs(node.right, depth+1, result)