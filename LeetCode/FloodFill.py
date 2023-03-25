class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        cols, rows = len(image), len(image[0])
        orgCol = image[sr][sc]
        #Recursive input of [x,y]
        def fillEach(x, y):
            if image[x][y] == newColor or image[x][y] != orgCol:
                return
            else:
                image[x][y] = newColor
            if x + 1 < cols:
                fillEach(x+1, y)
            if y + 1 < rows:
                fillEach(x, y+1)
            if x - 1 >= 0:
                fillEach(x-1, y)
            if y - 1 >= 0:
                fillEach(x, y-1)
        
        fillEach(sr,sc)
        return image
