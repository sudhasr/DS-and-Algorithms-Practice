"""200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

"""
"""
Approach1: BFS iterative approach using queue
1. Traverse the grid and add the coordinate whose has value if land '1' into a queue and increase count by 1. Mark that coordinate as visited by changing its value to '0'.
2. Process the element in the queue by checking its neighbors using directions array, add a neighbor whose value is a land. Also, mark visited on neighboring lands.
3. Once all elements in queue is processed, continue traversing the grid and repeat the process of incrementing count and checking neighbors when you find another land.
4. when whole grid is processed, return count.
"""
# Time Complexity - O(n x m) as we are traversing and checking every coordinate once
# Space Complexity - O(m x n) as we create a queue and worst case if all the values are '1'


from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge Case
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        count = 0
        q = deque()
        n = len(grid)
        m = len(grid[0])
        # Directions array for ease of neighbor traversal
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Up, Right , Down, Left
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    q.append([i, j])
                    grid[i][j] = '0'# Mark as visited
                    while q:
                        curr = q.popleft()
                        #Traverse in four directions to find neighboring lands
                        for d in dirs:
                            r = d[0] + curr[0]
                            c = d[1] + curr[1]
                            # Checking boundary conditions and if it is a land
                            if r >= 0 and r < n and c >=0 and c < m and grid[r][c] == '1':
                                q.append([r, c])
                                grid[r][c] = '0'
        return count
		
"""
Approach1: DFS recursiver approach
1. Traverse the grid and when we find value as '1', call dfs function and increase count by 1. 
2. In the dfs recrusive function, mark that coordinate as visited by changing its value to '0'.
3. Declare the directions array in the global scope and calculate the neighbors of the current i,j coordinates in recrusive function
4. For each newly calculated coordinate, check the boundary conditions and check if it is land. Call the recursive function only on those satisfying coordinates
5. When recursion exits, it means we need increment coordinates of the grid and repeat the process of checking neighbors recrusively
6. When whole grid is processed, return count.
"""
# Time Complexity - O(n x m) as we are traversing and checking every coordinate once
# Space Complexity - O(1) without considering recursive stack and O(m x n) if we consider recursive stack and worst case if all the values are '1'

# Global scope declaration
# Directions array for ease of neighbor traversal
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] # Up, Right , Down, Left

class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge Case
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        count = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,n,m,i,j)
        return count
        
    def dfs(self, grid, n, m, i, j):
        # No need to have separate base case as we will not be breaking the condition by finding '0'
        
        # Mark as visited
        grid[i][j] = '0'
        
        for d in dirs:
            r = d[0] + i
            c = d[1] + j
            
            # Checking boundary condition and covering base case here
            if r >= 0 and r < n and c >= 0 and c < m and grid[r][c] == '1':
                self.dfs(grid,n,m,r,c)