import collections as c

# Is it possible for a less expensive project to return less profit? yes

class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # For a given sort profits by maximum profit, then

        proj = zip(capital, profits)
        proj.sort()

        #Set the avaiable project pointer
        availProj=0

        availProj = c.deque()


        # Add the first element?
        maxProfit=0
        for i in range(len(proj), 0, -1):
            if proj[i][0] < w:
                if maxProfit < proj[i][1]:
                    maxProfit = proj[i][1]
                availProj.append(proj[0])



        for i in k:
            for i in proj:
                if w >= proj[1][0]:
                    #Find maximum of profit

                    continue
            
        return w
