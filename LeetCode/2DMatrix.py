import collections
import math

class Solution:

    #DFS to use stack
    #BFS to use queue

    # To use BFS (OR DP Subproblem)
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix)-1
        cols = len(matrix[0])-1

        iPivot = 0
        jPivot = 0 

        q = collections.deque()
        
        #Binary search j
        # Find the row (jPivot) that has the minimum start value for the target
        while True:
            if jPivot == rows:
                break
            mid = int((rows - jPivot)/2)
            if matrix[mid][1] <= target:
                jPivot = mid 
            if target < matrix[mid][1]:
                if matrix[mid + 1]:

                    if target <matrix[mid + 1][1]:
                        pass
                    else:
                        pass
                rows = mid 
            print("Row : ", rows, " jPivot: ", jPivot)

        if target < jPivot:
            return False
        #Binary Search the single row
        row = matrix[jPivot]
        while True:
            mid = int((cols-iPivot)/2)
            if target == row[iPivot]:
                return True
            elif cols == iPivot:
                return False
            elif row[mid] <= target:
                iPivot = mid
            else :
                cols = mid
            print("Col : ", cols, " iPivot: ", iPivot)        


sol = Solution()

cases = [([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)]

for i in cases:
    print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

