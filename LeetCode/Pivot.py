# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        pivot = ((start + n)/2)
        while start != n :
            pivot = ((start + n)/2)
            if (isBadVersion(pivot)):
                n= pivot
            else:
                start = pivot+1

        return n