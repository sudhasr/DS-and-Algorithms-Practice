# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        self.target = sum
        temp = []
        #dfs
        self.helper(root, 0, temp)
        return self.result
    
    def helper(self, root, currsum, temp):
        # Base Case
        if root == None:
            return
        if root.left == None and root.right == None:
            currsum += root.val
            temp.append(root.val)
            print(temp)
            if currsum == self.target:
                self.result.append(temp[:])
            temp.pop()
            return     
            
        # Action
        currsum += root.val
        temp.append(root.val)
        print(temp)
        
        # Recursion
        self.helper(root.left, currsum, temp)
        self.helper(root.right, currsum, temp)
        
        # Backtracking
        temp.pop()
        return
        
        