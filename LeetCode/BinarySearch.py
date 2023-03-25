class Solution(object):
    def search(self, nums, target):
        # nums = [a,b,c,d,e]
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #print nums

        #If no numbers left
        if (len(nums) == 1):
            if nums[0] == target:
                return 0
            else: return -1
        
        # Start index at halfway
        index = (len(nums)/2)
        
        # if number is in first half
        if (nums[index] == target):
            return index
        elif (nums[index] > target):    
            result = self.search(nums[0:index], target)
            #print(result)
            # add result to the index

        # search second half 
        else: 
            result = self.search(nums[index:], target)
            #print(result)
            if (result != -1):
                result = index + result
                #print("+", index)
        return result
        