class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cols, rows = len(grid[0]), len(grid)
        
        # for each startpoint
        
        # ignore previously visited points
        visited = set()
        
        maxSize = 0

        def getNeighbour(x,y):
            sums = 0
            #TODO: Change to -1 and return immediately in recursive check
            if (x, y) in visited:
                return 0
            visited.add((x,y))
            
            if (grid[x][y]) != 1:
                return 0
            sums += 1

            if (x + 1) < rows:
                sums += getNeighbour(x+1, y)
            if (y + 1) < cols:
                sums += getNeighbour(x, y+1)
            if (x - 1) >= 0:
                sums += getNeighbour(x-1, y)
            if (y - 1) >= 0:
                sums += getNeighbour(x, y-1)
                
            return sums
        
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if (i,j) in  visited:
                    j += 1
                    continue
                size = getNeighbour(i,j)
                if size > maxSize:
                    maxSize = size
                j += 1
            i += 1
        
        return maxSize