class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #Brute Force
        
        # Count the number of characters that match
        match =0
        
        #One pointer for each of the strings
        #The subsequent characters in s1 must start from the subsequent index in s2
        
        i = 0
        j = 0
        
        while i < len(s2):
            print(i, j, match)
            if s1[j] == s2[i]:
                match += 1
                j += 1
            # Try the next character in the set
                
            i += 1
            
        if match == len(s1):
            return True
        else:
            return False