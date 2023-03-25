class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols, rows = len(grid[0]), len(grid)
        
        visited = [[False for i in range(cols)] for i in range(rows)]
        
        def findIsland(y,x):
            if visited[y][x]:
                return False
            visited[y][x] = True
            if grid[y][x] != "1":
                return False
            if y+1 < rows:
                findIsland(y+1, x)
            if x+1 < cols:
                findIsland(y, x+1)
            if y-1 >= 0:
                findIsland(y-1, x)
            if x-1 >= 0:
                findIsland(y, x-1)
            return True
        islands = 0
        i = 0
        
        while i< rows:
            j = 0
            while j < cols:
                if findIsland(i,j):
                    islands += 1
                j+=1
            i+=1
        return islands
            
            