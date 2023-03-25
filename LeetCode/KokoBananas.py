import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        """
        Upper and lower bounds of the problem
        
        with n piles she will minimally have to do n runs
        in h hours
        i.e. she has to visit each bucket at least once
        
        min rate = n/h
        
        max rate is eating whole pile each time i.e. max(piles) n hours
        
        therefore if h=n, then its just the max(piles)
        """
        h= int(h)
        if h <= len(piles):
            return max(piles)
        
        rates = range(int(len(piles)//h), max(piles))
        leftIndex = len(piles)//h
        rightIndex = max(piles)
        lastSln = None

        while True:
            rate = float((rightIndex+leftIndex)//2)
            #Rate goes to (1+2)/2 = 1, then it becomes equal

            # Two parts
            # 1. if solution already found, optimising for lower
            # 2. if no solution found yet then increase number


            print(leftIndex, rightIndex, rate)
            #1. If Solution found, but optimising for minimum 
            if None != lastSln:
                #already at minimum
                if rate == leftIndex:
                    return rate
                else:
                    rate -= 1
            time = 0
            for i in piles:
                time += math.ceil(i/rate) 
                # print(time)
            rate = int(rate)
            if time == h:
                lastSln = rate
                rightIndex = rate
                # One banana a time is too slow!!
            elif time > h:
                #If taking too much time, increase eat rate
                leftIndex = rate
                print(time)

            else:
                rightIndex = rate


soln = Solution()
print(soln.minEatingSpeed([9999], 9998))