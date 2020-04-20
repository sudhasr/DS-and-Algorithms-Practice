"""
515. Find Largest Value in Each Tree Row

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

"""
"""
Approach1: BFS iterative approach using queue
1. Create a queue, add the root into queue, until queue is true (has element(s)), start level processing.
2. To keep track of levels, calculate the size of the queue, iterate the elementsfor that size although more elements could be present in the queue
3. Besides the size calculation, also initialize/reset the max_val to be minus infinity at beginning of processing each level
4. Pop the root element, compare its value with max_val. If it is greater, update max_val.
5. Cehck if the root node has children, if it does then add them to the queue and repeat same process by popping each node from queue
"""
# Time Complexity - O(N) as we are traversing every node
# Space Complexity - O(N) as we use queue and at a time max size of the queue could be max element at a level 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # Edge Case
        if root == None:
            return []
        
        result = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            # Reset max_val for every level
            max_val = float('-inf')#minus infinity
            for i in range(size):
                curr = q.popleft()
                if curr.val > max_val:
                    max_val = curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            # Update result array at the end of each level
            result.append(max_val)
        return result


"""
Approach1: DFS recursive approach
1. Have a depth variable initialized to zero and result array to hold max values
2. Make recursive call by passing root value, depth of tree where we are processing and result array (modified at every level)
3. The strategy is to compare depth value and size of result array. If depth is equal to size of result, then it means we have
	not processed the level yet. In this case, we need to add node value to the result array. This case will happen when we are going down the nodes of the tree.
4. When we reach Null (leaf node), we need to come back to previuos recursive call, this time we check if node has right child. When we process the right child, it means 
	we are processing another node at previuosly processed depth. So here size of result will not be equal to depth. Now we need to compare the current 
	node value with the value of result array at the index equal to depth i.e., result[depth]. If it is greater, update the value in result array
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity - O(N) as we traverse every node in the tree
# Space Complexity - O(N) where N is equal to maxDepth

# DFS
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # Edge Case
        if root == None:
            return []
        
        result = []
        # dfs recursive call
        self.__dfs(root, 0, result)
        return result
    
    # Using a private helper function
    # OOPs principle - Abstraction
    def __dfs(self, node, depth, result):
        # Base Case (Not really required as we will never reach this condition since we are calling recursive function only if node.left and node.right exists)
        if node == None:# Leaf node
            return
        # Compare the depth value and size of result array
        if depth == len(result):
            result.append(node.val)
        else:
            if node.val > result[depth]:
                result[depth] = node.val                
            
        if node.left:
            self.__dfs(node.left, depth+1, result)
        if node.right:
            self.__dfs(node.right, depth+1, result)
			
""" Wrong answer """
"""
I encountered an interesting problem here.


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # Edge Case
        if root == None:
            return []
        
        result = []
        # dfs recursive call
        self.__dfs(root, 0, []) #Pass result instead of [] for correct answer
        return result
    
    # Using a private helper function
    # Abstraction principle is implemented here
    def __dfs(self, node, depth, result):
        # Base Case
        
        # Compare the depth value and size of result array
        if depth == len(result):
            result.append(node.val)
        else:
            if node.val > result[depth]:
                result[depth] = node.val                
            
        if node.left:
            self.__dfs(node.left, depth+1, result)
        if node.right:
            self.__dfs(node.right, depth+1, result)