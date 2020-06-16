'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. An island is surrounded by
water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Leetcode 200
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        visited = [[False for _ in range(c)] for _ in range(r)]
        
        count = 0


        def dfs ( i,j):
            if i < 0 or j <0 or i >=r or j>=c or grid[i][j]== '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs( i-1,j)
            dfs(i+1,j)
            dfs( i,j+1)
            dfs( i , j-1)
            
        
        for x in range(r):
            for y in range(c):
                if not visited[x][y] and grid[x][y]== '1':
                    dfs(x,y)
                    count +=1
                    
        return count        
