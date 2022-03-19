class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #swap each of the elements four times
        #keep track of the first swapped element
        #Edges swap [0,0] with [n,0] with [n,n] with [0,n]
        #for i in range(n) for j in range(n): 
        # [i,j] swapped wth [n-j, i] with [n-i, n-j] with [j, n-i]
        


        n = len(matrix)-1
        first=0
        yran= range((n+1)/2)
        xran= range((n+2)/2)
        for i in xran:
            for j in yran:
                # a = matrix[i][j]
                # b= int(matrix[n-j][i])
                # c= int(matrix[n-i][n-j])
                # d= int(matrix[j][n-i])
                first = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i]= matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = first